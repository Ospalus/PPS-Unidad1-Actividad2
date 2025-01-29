# 1. Función para sumar dos números
def suma(a, b):
    """
    Función que toma dos números 'a' y 'b' y devuelve la suma de ambos.
    """
    return a + b

# 2. Función para restar dos números
def resta(a, b):
    """
    Función que toma dos números 'a' y 'b' y devuelve la resta de 'a' menos 'b'.
    """
    return a - b

# 3. Función para multiplicar dos números
def multiplicacion(a, b):
    """
    Función que toma dos números 'a' y 'b' y devuelve el producto de ambos.
    """
    return a * b

# 4. Función para dividir dos números
def division(a, b):
    """
    Función que toma dos números 'a' y 'b' y devuelve el cociente de 'a' dividido entre 'b'.
    Si 'b' es 0, devuelve un mensaje de error.
    """
    if b == 0:
        return "Error: División por cero no permitida."
    else:
        return a / b

# 5. Función para verificar si un valor es un número
def isNumber(valor):
    """
    Función que verifica si el argumento 'valor' es un número.
    """
    try:
        float(valor)  # Intentamos convertir a float
        return True
    except ValueError:
        return False

# 6. Función para verificar si un número es mayor que cero
def mayorCero(valor):
    """
    Función que verifica si el número 'valor' es mayor que cero.
    """
    return valor > 0

# Función principal para interactuar con el usuario
def calculadora():
    # Pedimos al usuario que ingrese dos números
    num1 = input("Ingrese el primer número: ")
    num2 = input("Ingrese el segundo número: ")

    # Verificamos si los valores ingresados son números
    if not isNumber(num1) or not isNumber(num2):
        print("Por favor, eso no son números!! Ingrese números válidos.")
        return  # Salimos de la función si los números no son válidos

    num1 = float(num1)
    num2 = float(num2)

    # Verificamos si los números son mayores que cero
    if not mayorCero(num1) or not mayorCero(num2):
        print("Uno o ambos números no son mayores que cero.")
        return  # Salimos de la función si los números no son mayores que cero

    # Menú de operaciones
    print("\nSeleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    # Pedimos la opción al usuario
    opcion = input("Ingrese el número de la operación que desea realizar: ")

    # Ejecutamos la operación correspondiente
    if opcion == '1':
        print(f"\nResultado: {suma(num1, num2)}")
    elif opcion == '2':
        print(f"\nResultado: {resta(num1, num2)}")
    elif opcion == '3':
        print(f"\nResultado: {multiplicacion(num1, num2)}")
    elif opcion == '4':
        print(f"\nResultado: {division(num1, num2)}")
    elif opcion == '5':
        print("Saliendo del programa.")
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 5.")

# Ejecutar la calculadora
calculadora()
