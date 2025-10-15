import agenda as ag

def mostrar_menu ():
    print ("\n   - MENU PRINCIPAL -")
    print ("1. Añadir o/ Modificar")
    print ("2. Buscar")
    print ("3. Eliminar")
    print ("4. Salir")


# programa principal

while True:
    mostrar_menu()
    opcion = input (" Ingrese la opción validad ( 1 - 4):  ")
    
    if opcion == "1": 
        dni = int (input (" Ingrese el DNI: "))
        ag.anadir_modificar(dni)
    elif opcion == "2":
        cadena = input (" Ingrese el nombre a buscar:  ")
        ag.buscar_nombre (cadena)
    elif opcion == "3":
        dni = int (input (" Ingrese el DNI: "))
        ag.borrar (dni)
    elif opcion == "4":
        print (" Salir")
        break
    else: 
        print (" Opcion invalidad. Intenta de nuevo")
