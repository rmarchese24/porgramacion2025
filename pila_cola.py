# Pila (stack) LIFO

pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print("Pila ", pila)

sacar_elemento = pila.pop()
print (" Elemento sacado de la pila es  ", sacar_elemento)
print("Pila despues de pop ", pila)


# Cola (queue) FIFO

cola = [] # cola vacia
cola.append(1)
cola.append(2)
cola.append(3)

print ("Cola: " , cola)
sacar_elemento_cola = cola.pop(0) # ubicacion del elemento a sacar

print ("Cola despues de pop: " , cola)

# libreria deque
