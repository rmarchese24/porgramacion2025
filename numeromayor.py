# Ingrese tres numeros y verifique cual es el mayor, al final mostrar el numeros. 

num1 = int (input (" Ingrese el primer numero"))
num2 = int (input (" Ingrese el segundo numero"))
num3 = int (input (" Ingrese el tercer numero"))

"""if num1>num2 and num1>num3:
    mayor = num1
else:
    if num2>num3:
        mayor = num2
    else: 
        mayor = num3 

print ("El mayor es   " , mayor)
"""

if num1>num2 and num1>num3:
    mayor = num1
elif num2>num3:
    mayor = num2
else: 
    mayor = num3 


print (f"El mayor es:   {mayor}")