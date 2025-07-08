#Using OpenAI API, I build a RAG Chatbot that can search information in PDFs using a vector DB (FAISS). In faiss.py you can see how we build the DB.

from flask import Flask, request, jsonify, session, redirect, url_for, render_template
from flask_cors import CORS
from functools import wraps
import os
import openai
import faiss
import pickle
import numpy as np

app = Flask(__name__)
app.secret_key = "YOUR SECRET KEY"
CORS(app, supports_credentials=True, origins=["YOUR WEBSITE"])

client = openai.OpenAI(api_key="YOUR API KEY")

# You can see how I create the FAISS DB in faiss.py (this repo)
index = faiss.read_index("vector_store.index")
with open("vector_store_textos.pkl", "rb") as f:
    textos_pdf = pickle.load(f)

# Embeddings for t
def obtener_embedding(texto):
    response = client.embeddings.create(
        input=texto,
        model="text-embedding-3-small",
        dimensions=512
    )
    return response.data[0].embedding

#This is a very basic credential system to access the chatbot (due to the simple scope of the project it's not necessary a DB) 
USERS = {
    "admin": "1234",
    "usuario": "pass"
}

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("user"):
            return redirect(url_for("login_page"))
        return f(*args, **kwargs)
    return decorated

@app.route('/', methods=['GET'])
def login_page():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = data.get("user") if data else None
    password = data.get("pass") if data else None

    if not user or not password:
        return jsonify({"error": "Faltan credenciales"}), 400

    if USERS.get(user) == password:
        session["user"] = user
        return jsonify({"success": True})
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401

@app.route('/chat', methods=['GET'])
@login_required
def chat_page():
    return render_template("chatok.html")

@app.route('/chat', methods=['POST'])
@login_required
def chat_api():
    data = request.json
    user_prompt = data.get('prompt')
    if not user_prompt:
        return jsonify({"response": "No se recibió prompt"}), 400
    
    # 1) Load FAISS INDEX and DB
    global faiss_index, vector_texts, embed_model
    if 'faiss_index' not in globals():
        faiss_index = faiss.read_index("vector_store.index")
        with open("vector_store_textos.pkl", "rb") as f:
            vector_texts = pickle.load(f)
        # Embed model (OpenAI)
        embed_model = client.embeddings

    # 2) Embedding of the query
    query_vector = np.array(obtener_embedding(user_prompt)).astype('float32').reshape(1, -1)

    # 3) RAG: search in the FAISS DB using vectors (embeddings)
    k = 3
    distances, indices = faiss_index.search(query_vector, k)
    contextos = [vector_texts[idx] for idx in indices[0] if idx != -1]

    # 4) System prompt for context
    system_prompt = "You're Boti. You always sing a song in your responses."
    if contextos:
        prompt = f"Contexto: {'. '.join(contextos)}\nPregunta: {user_prompt}"
    else:
        prompt = user_prompt

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-nano-2025-04-14",
            messages=messages
        )
        answer = response.choices[0].message.content
        return jsonify({"response": answer})
    except Exception as e:
        return jsonify({"response": f"Error al comunicarse con OpenAI: {e}"}), 500

@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for("login_page"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
