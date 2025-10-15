"""frutas = ["manzana", "bananas" ,"pera", "naranja"]
try:
    indice = int (input (" Ingresa un numero del 0 al 3 para ver la fruta"))
    print (f" La fruta seleccionada es : {frutas [indice]}")
except IndexError:
    print (" El indice no es correcto los valores son  0 a 3")
except ValueError:
    print (" Debes ingresar un numero entero ")
"""

# Version Exception
frutas = ["manzana", "bananas" ,"pera", "naranja"]
try:
    indice = int (input (" Ingresa un numero del 0 al 3 para ver la fruta"))
    print (f" La fruta seleccionada es : {frutas [indice]}")
except Exception as error:
    print (f"El error es: {type(error)}")

