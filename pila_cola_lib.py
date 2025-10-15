#deque

from collections import deque

pila = deque()
pila.append(1)
pila.append(2)
pila.append(3)
print("Pila ", pila)

sacar_elemento = pila.pop()
print (" Elemento sacado de la pila es  ", sacar_elemento)
print("Pila despues de pop ", pila)

# Cola (queue) FIFO

cola = deque() # cola vacia
cola.append(1)
cola.append(2)
cola.append(3)

print ("Cola: " , cola)
sacar_elemento_cola = cola.popleft # ubicacion del elemento a sacar

print ("Cola despues de pop: " , cola)

# libreria deque

# atencion cliente

cola_clientes = deque (["Juan", "Pedro", "Maria", "JOse"])

while cola_clientes: 
    cliente = cola_clientes.popleft()
    print (f"Atendiendo al cliente : {cliente}")
    
    