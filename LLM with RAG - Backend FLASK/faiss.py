import os
import pdfplumber #I recommend pdfplumber over PyPdf, I always get better results.
import openai
from openai import OpenAI
import faiss
import pickle
import tiktoken

from typing import List

client = OpenAI(api_key = "YOUR API KEY")

# Divide the text of the PDFs in 3000 chars chunks
def dividir_texto(texto, max_chars=3000):
    return [texto[i:i+max_chars] for i in range(0, len(texto), max_chars)]

# Text to embedding (vectors)
def obtener_embedding(texto):
    response = client.embeddings.create(
    input=texto,
    model="text-embedding-3-small",
    dimensions=512
    )
    return response.data[0].embedding

# 1. Extract the text of the PDFs
def extraer_texto_pdfs(directorio):
    textos = []
    for archivo in os.listdir(directorio):
        if archivo.endswith(".pdf"):
            ruta = os.path.join(directorio, archivo)
            with pdfplumber.open(ruta) as pdf:
                texto = ""
                for pagina in pdf.pages:
                    texto += pagina.extract_text() or ""
                textos.extend(dividir_texto(texto))
    return textos

# 2. Create FAISS DB
def crear_base_vectorial(textos):
    embeddings = [obtener_embedding(texto) for texto in textos]
    dimension = len(embeddings[0])
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings).astype('float32'))
    return index, textos

# 3. Save FAISS DB as .pkl and DB index as .index
def guardar_base(index, textos, nombre_base="vector_store"):
    faiss.write_index(index, f"{nombre_base}.index")
    with open(f"{nombre_base}_textos.pkl", "wb") as f:
        pickle.dump(textos, f)

# 4. Run
if __name__ == "__main__":
    import numpy as np
    carpeta_pdfs = os.path.join(os.path.dirname(__file__), "pdfs")
    textos = extraer_texto_pdfs(carpeta_pdfs)
    index, textos = crear_base_vectorial(textos)
    guardar_base(index, textos)
    print("FAISS DB OK.")
