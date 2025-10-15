#Ejercicio 1 Matriz y funciones Suma Filas y columnas de la matriz
#1) solicite al usuario las dimensiones de una matriz ( numero de filas y columnas)
#2) permita ingresar los valores de la matriz 
#3) muestre la matriz de forma tabular 
#4) Calular los siguentes datos:
    # La suma de cada fila, la suma de cada columna y el total general 
#2)
def cargar_matriz(filas, columnas):   
    matriz = []
    print("\nIngresá los valores de la matriz")
    for i in range (filas):
        fila = [] 
        for j in range (columnas):
            valor = int(input(f"Ingrese el valor en posición [{i}] x [{j}]:     "))
            fila.append(valor)
        matriz.append (fila)
    return matriz

#3) Tabular
def mostrar_matriz (matriz):
    print ("\nMatriz ingresada")
    for fila in matriz:
        linea = ""
        for valor in fila:
            linea += str(valor) + "\t"
        print(linea)
        
def mostrar_matriz1 (matriz):
    print ("\nMatriz ingresada")
    for fila in matriz:
       print( "\t".join(str(x) for x in fila))
       
def suma_filas (matriz):
    print("\nSuma De filas: ")
    suma=0
    for fila in matriz:
        suma =0
        for valor in fila:
            suma+=valor
            #print(f"la Suma por elementos es:  {suma}")
        print(f"la Suma por fila es {fila}:  {suma}")
    
          
def suma_columnas (matriz):
    print("\nSuma De columnas: ")
    suma=0
    for j in range(columnas):
        suma = sum (matriz[i][j] for i in range(filas))
            #print(f"la Suma por elementos es:  {suma}")
        print(f"la Suma por columna es {j}:  {suma}")
           
def total_matriz (matriz):
    total = sum (sum(i) for i in matriz)
    print(f"\nSuma total es : {total}")
        




# Programa Principal 
#1)
filas = int (input("Ingrese la cantidad de filas:    "))
columnas = int (input("Ingrese la cantidad de columnas:   "))
matriz= cargar_matriz (filas, columnas)
print (matriz)
mostrar_matriz(matriz)
mostrar_matriz1(matriz)
suma_filas(matriz)
suma_columnas(matriz)
total_matriz(matriz)