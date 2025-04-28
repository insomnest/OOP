def calculator():
    while True:
        print("\nCalculadora")
        print("1. Suma (+)")
        print("2. Resta (-)")
        print("3. Multiplicación (*)")
        print("4. División (/)")
        print("5. Salir")

        choice = input("Seleccione una opción (1-5): ")

        if choice == "5":
            print("Saliendo de la calculadora...")
            break

        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if choice == "1":
            result = num1 + num2
        elif choice == "2":
            result = num1 - num2
        elif choice == "3":
            result = num1 * num2
        elif choice == "4":
            result = num1 / num2 if num2 != 0 else "Error: División por cero no permitida."
        else:
            print("Opción inválida. Intente nuevamente.")
            continue

        print(f"Resultado: {result}")

calculator()
