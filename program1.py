def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

def suma_n(n):
    if n == 0 or n == 1:
        return n
    else:
        return n+suma_n(n-1)

def fibonacci(n):
    if n == 0:
        return 0
    else:
        if n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

def contar_letra(palabra, letra, i=0):
    if i == len(palabra) or letra == "":
        return 0
    else:
        if palabra[i] == letra:
            return 1 + contar_letra(palabra, letra, i+1)
        else:
            return contar_letra(palabra, letra, i+1)

def invertir_cadena(cadena, i=0):
    if i == len(cadena):
        return ""
    else:
        return invertir_cadena(cadena, i+1) + cadena[i]

def potencia(n,e):
    if e == 0:
        return 1
    else:
        return n*potencia(n,e-1)

while True:
    print("\n- MENU DE RECURSIVIDAD -")
    print("1- Factorial de n")
    print("2- Suma de numeros n")
    print("3- Fibonacci de n")
    print("4- Repetición de letra en cierta palabra")
    print("5- Invertir cadena de texto")
    print("6- Potencia")
    print("7- Salir")

    option_user = input("Ingresa una opcion: ")

    match option_user:
        case "1":
            print("\nFactorial de numero n")
            n = int(input("Ingresa un numero: "))
            print(f"El factorial de {n}, es: {factorial(n)}")

        case "2":
            print("\nSuma de numeros n")
            n = int(input("Ingresa un numero: "))
            print(f"El suma de numeros n = {suma_n(n)}")

        case "3":
            print("\nFibonacci de n")
            n = int(input("Ingresa un numero: "))
            print(f"El término {n} de Fibonacci es: {fibonacci(n)}")

        case "4":
            print("\nRepeticion de letra")
            palabra = input("Ingrese la palabra que desea:").lower()
            letra = input("Ingrese la letra que desea buscar en la palabra: ").lower()
            print(f"La letra '{letra}' aparece {contar_letra(palabra, letra, 0)} veces")

        case "5":
            print("\nInvertir cadena de texto")
            cadena = input("Ingresa una cadena: ")
            print(invertir_cadena(cadena, 0))

        case "6":
            print("\nPotencia")
            n = int(input("Ingresa un numero: "))
            e = int(input("Ingresa el exponente: "))
            print(f"El resultado de {n}^{e} es: {potencia(n,e)}")

        case "7":
            print("\nSaliendo del programa")
            break

        case _:
            print("\nError, intente de nuevo.")
