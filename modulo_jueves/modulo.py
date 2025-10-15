import modulo1
import os
import time

os.system ("cls")
valor1 = float (input (" Ingrese el primer valor : "))
valor2 = float (input (" Ingrese el segundo  valor : "))

time.sleep(2)
resultado = modulo1.f_sumar(valor1, valor2)
print(f"la suma de los valores ingresados : {resultado}")

time.sleep(2)
resultado1= modulo1.f_restar(valor1,valor2)
print(f"la resta de los valores ingresados : {resultado1}")

time.sleep(5)

os.system ("cls")