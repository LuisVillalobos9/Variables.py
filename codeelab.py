# Variables de diferentes tipos
cadena = "Hola"
entero = 42
flotante = 3.1416
booleano = True

#Es importante convertir las variables numericas a cadenas antes de concantenarlas 
resultado_concatenacion = cadena + " " + str(entero) + " " + str(flotante) + " " + str(booleano)


# 1. Limite de los enteros y flotantes en Python:
# Python no tiene un maximo para los numeros enteros ya que todo depende de la memoria disponible
# Para los flotantes, Python utiliza el estandar IEEE 754 de 64 bits (float) que tiene de tamaño y precision
# El rango de valores para float es de aproximadamente 1.7 * 10^¨-308 a 1.7^308


# 2. La formula para la suma de los primeros n numeros pares:
# La suma de los primeros n numeros pares es n * (n + 1)
numero_entero = 10 # Seleccionamos 10 como ejemplo de n
suma_pares= numero_entero * (numero_entero + 1)

# Imprecion de todos mis resultados 
print("Resultado de la concatenacion:", resultado_concatenacion)
print("Limite de los enteros en Python: No hay limite maximo (depende de la memoria).")
print("Limite de los flotantes en Python: Rango de aproximadamente 1.7 * 10^-308 a 10^308")
print("Suma de los primeros", numero_entero, "numeros pares", suma_pares)

#Gracaias:D