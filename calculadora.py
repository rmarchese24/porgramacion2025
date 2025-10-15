import math
import time

def mostrar_menu():
    print("\n--- CALCULADORA CIENTÍFICA ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Raíz cuadrada")
    print("6. Potencia")
    print("7. Logaritmo base 10")
    print("8. Seno (en grados)")
    print("9. Coseno (en grados)")
    print("0. Salir")

def pausa():
    print("Calculando...")
    time.sleep(1)

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "0":
        print("¡Hasta luego!")
        break

    elif opcion in ["1", "2", "3", "4", "6"]:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        pausa()

        if opcion == "1":
            print(f"Resultado: {num1 + num2}")
        elif opcion == "2":
            print(f"Resultado: {num1 - num2}")
        elif opcion == "3":
            print(f"Resultado: {num1 * num2}")
        elif opcion == "4":
            if num2 != 0:
                print(f"Resultado: {num1 / num2}")
            else:
                print("Error: No se puede dividir por cero.")
        elif opcion == "6":
            print(f"Resultado: {math.pow(num1, num2)}")

    elif opcion == "5":
        num = float(input("Ingresa un número: "))
        if num >= 0:
            pausa()
            print(f"Resultado: {math.sqrt(num)}")
        else:
            print("Error: No se puede calcular la raíz cuadrada de un número negativo.")

    elif opcion == "7":
        num = float(input("Ingresa un número positivo: "))
        if num > 0:
            pausa()
            print(f"Resultado: {math.log10(num)}")
        else:
            print("Error: El número debe ser mayor que cero.")

    elif opcion == "8":
        grados = float(input("Ingresa el ángulo en grados: "))
        pausa()
        print(f"Seno: {math.sin(math.radians(grados))}")

    elif opcion == "9":
        grados = float(input("Ingresa el ángulo en grados: "))
        pausa()
        print(f"Coseno: {math.cos(math.radians(grados))}")

    else:
        print("Opción no válida. Intenta de nuevo.")