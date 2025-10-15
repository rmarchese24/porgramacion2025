import numpy as np

def cargar_vector(n, nombre):
    aux = []
    for i in range(n):
        valor = int (input (f"Ingrese numero para vector {nombre}"))
        aux.append(valor)
    vect =np.array(aux)
    return vect

n=int(input( "ingrese la longitud del arreglo "))
A=cargar_vector( n, nombre ="A")
B=cargar_vector( n, nombre ="B")
print ("vECTOR a")
print (A)
print ("vECTOR B")
print (B)