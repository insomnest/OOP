class Calculadora:
    def __init__(self):
        self.opciones = {
            "1": ("Suma", self.suma),
            "2": ("Resta", self.resta),
            "3": ("Multiplicación", self.multiplicacion),
            "4": ("División", self.division),
            "5": ("Salir", None)
        }

    def ejecutar(self):
        while True:
            print("\nCalculadora")
            for key, (nombre, _) in self.opciones.items():
                print(f"{key}. {nombre}")

            opcion = input("Seleccione una opción (1-5): ")

            if opcion == "5":
                print("Saliendo de la calculadora...")
                break

            if opcion in self.opciones and opcion != "5":
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                resultado = self.opciones[opcion][1](num1, num2)
                print(f"Resultado: {resultado}")
            else:
                print("Opción inválida. Intente nuevamente.")

    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b if b != 0 else "Error: División por cero no permitida."


# Instancia y ejecución de la calculadora
calculadora = Calculadora()
calculadora.ejecutar()