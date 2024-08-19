#Using the NumPy libraries to create arrays and TensorFlow and Keras for neural networks (and some matplotlib to plot the training), 
#a machine learning algorithm is created. As can be seen in the code, at no point are the mathematical operations for converting 
#Celsius to Fahrenheit provided; instead, the algorithm automatically learns them from an array of Celsius degrees and their 
#corresponding Fahrenheit results.  At the end of the code, the user can input any temperature in Celsius, and the algorithm 
#will convert it to Fahrenheit.

import tensorflow as tf
import numpy as np

celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46.4, 59, 71.6, 100.4], dtype=float)

oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
oculta2 = tf.keras.layers.Dense(units=3)
salida = tf.keras.layers.Dense(units=1)
modelo = tf.keras.Sequential([oculta1, oculta2, salida])

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
)

print("Comenzando entrenamiento...")
historial = modelo.fit(celsius, fahrenheit, epochs=1000, verbose=False)
print("Modelo entrenado!")

# En el modelo se incluyen 1000 vueltas pero puede verse en el gráfico que con menos de
# 100 ya no tiene perdidas.
import matplotlib.pyplot as plt
plt.xlabel("# Epoca")
plt.ylabel("Magnitud de pérdida")
plt.plot(historial.history["loss"])
plt.show()

print("Variables internas del modelo")
print(oculta1.get_weights())
print(oculta2.get_weights())
print(salida.get_weights())

while True:
    print("Hagamos una predicción!")
    my_array = []
    my_array.append(float(input("Ingresa una temperatura celsius (o escribe 7000 para salir): ")))
    my_array = np.array(my_array)
    resultado = modelo.predict(my_array)
    if my_array == [7000]:
        break
    else:
        print("El resultado es " + str(resultado) + " fahrenheit!")
