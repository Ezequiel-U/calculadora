from calculator import suma, resta, multiplicacion, division

def menu():
    print("\n=== Calculadora ===")
    print("1) Sumar")
    print("2) Restar")
    print("3) Multiplicar")
    print("4) Dividir")
    print("5) Salir")

while True:
    menu()
    opcion = input("Elige una opción: ")

    if opcion == "5":
        print("Bye 👋")
        break

    try:
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))

        if opcion == "1":
            print("Resultado:", suma(a, b))
        elif opcion == "2":
            print("Resultado:", resta(a, b))
        elif opcion == "3":
            print("Resultado:", multiplicacion(a, b))
        elif opcion == "4":
            print("Resultado:", division(a, b))
        else:
            print("Opción inválida")

    except Exception as e:
        print("Error:", e)