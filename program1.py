def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def suma_n(n):
    if n==0 or n==1:
        return n
    else:
        return n+suma_n(n-1)

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

        case "4":
            print("\nRepeticion de letra")

        case "5":
            print("\nInvertir cadena de texto")

        case "6":
            print("\nPotencia")

        case "7":
            print("\nSaliendo del programa")
            break

        case _:
            print("\nError, intente de nuevo.")
