import os

import time

import numpy

import modulo_jueves.modulo1 as paquete


os.system ("cls")
valor1 = float (input( "Ingrese un valor"))
valor2 = float (input("ingrese otro valor "))

time.sleep(2)
resultado = paquete.f_sumar(valor1,valor2)
print (f"la suma de los {resultado}")

time.sleep(5)

os.system ("cls")