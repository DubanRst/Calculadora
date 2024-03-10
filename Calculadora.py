
def calculadora():
    print("Calculadora en Python")
    print("Funciones:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    
    opcion = input("Por favor, elija la funcion que quiera usar (1/2/3/4): ")

   
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    
    if opcion == '1':
        resultado = num1 + num2
        print("El resultado de la suma es:", resultado)
    elif opcion == '2':
        resultado = num1 - num2
        print("El resultado de la resta es:", resultado)
    elif opcion == '3':
        resultado = num1 * num2
        print("El resultado de la multiplicación es:", resultado)
    elif opcion == '4':
        if num2 != 0:  
            resultado = num1 / num2
            print("El resultado de la división es:", resultado)
        else:
            print("Error: Recuerda que no se puede dividir en cero")
    else:
        print("Opción inválida. Por favor, elija una opción válida.")

calculadora()
