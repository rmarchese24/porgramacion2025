"""def fibonacci(n):
    if n == 0:
    # CASO BASE 1
        return 0
    elif n == 1:
# CASO BASE 2
        return 1
    else:
# CASO RECURSIVO
        return fibonacci(n-1) + fibonacci(n-2)
# Pedir al usuario un número
n = int(input("Ingresá una posición: "))
# Mostrar el resultado
print("El valor en la posición", n, "es:", fibonacci(n))


def suma_lista (lista):
    if len(lista) == 0:
        return 0
    else: 
        return lista [0] + suma_lista (lista[1:])
    

# bloque principal 
numeros = [4, 8, 10, 11]
print (" Suma Lista con recursividad:  ", suma_lista(numeros))

"""
def cuenta_regresiva (n):
    if n == 0:   # Caso base
        print ("¡ Despegue o Salida")
    else : 
        print (f"{n}.....")
        cuenta_regresiva (n-1)


# programa principal 
num = int (input(" Ingrese el numero para realizar la cuenta regresiva con recursividad"))
cuenta_regresiva (num)

