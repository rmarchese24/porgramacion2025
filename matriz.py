# Suma de diagonal de una matriz 
matriz = [ 
        [1,2,3],
        [2,5,1],
        [6,5,1]    ]

suma=0
i=0
while(i<len(matriz)):
    fila=matriz[i]
    j=0
    while(j<=len(fila)):
        if i==j:
            suma+=fila[j]
        j+=1
    i+=1
   
       
print(f"La suma de los elementos de la diagonal es: {suma}")

#Matriz en Python

# sumar elementos de la matriz
matriz = [ [1,2,3], [2,5,1],[6,5,1] ]

print(len(matriz))

suma=0
for fila in matriz:
    for valor in fila:
        print("elemento:", valor)
        suma+=valor
        #print(f"la Suma por elementos es:  {suma}")
    print(f"la Suma por fila es:  {suma}")
       
print(f"La suma de los elementos de la matriz es: {suma}")