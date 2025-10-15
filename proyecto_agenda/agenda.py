# creamos un diccionario vacio nombre de agenda

agenda = {}

"""Añadir/modificar: Nos pide un DNI. Si el DNI se encuentra en la agenda, debe mostrar los datos
de la persona y, opcionalmente, permitir modificarlos. Si el DNI no se encuentra, debe permitir
ingresar los datos de la persona correspondiente."""

def anadir_modificar (dni):
    if dni in agenda: 
        print (f" Dni encontrado : {dni} = {agenda}")
        opcion = input (" Deseás modificar los datos? (s/n)").lower()
        if opcion != "s": 
            return
    nombre = input ("Nombre : ")
    apellido = input ("Apellido: ")    
    telefono = input ("Telefono: ")
    email = input ("Email : ")
    edad = int (input ("Edad: "))    
    
    datos_personales ={ "Nombre":nombre,
                        "Apellido":apellido, 
                        "Telefono": telefono,
                        "Email":email,
                        "Edad": edad        
    }
    agenda[dni] = datos_personales
    print("Contacto guardado  /  modificado correctamente")
    print (agenda)

"""Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos
cuyos nombres comiencen por dicha cadena."""

def buscar_nombre (cadena):
    cadena = cadena.lower()
    print (f" Buscando los contactos que comiencen con {cadena}: ")
    for dni, datos_personales in agenda.items():
        nombre = datos_personales ["Nombre"].lower()
        if nombre.startswith(cadena):
            print (f"Los datos son : {agenda [dni]}")
        else: 
            print (f"Los datos no se encuentra   {cadena}")
   
    
        

"""Borrar: Nos pide un dni y si existe nos preguntará si queremos borrarlo de la
agenda. del"""
    
def borrar (dni): 
    if dni in agenda: 
        del agenda[dni]
        print(f" los datos del DNI : {dni} fueron eliminados")
    else: 
        print(f" los datos del DNI : {dni} no encuentra")
    
