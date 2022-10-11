import funciones

# Se pregunta la operación que el usuario desea tomar
option = input("¿Qué operación quieres hacer?\n1) Sumar\n2) Restar\n3) Negar\n4) Comparar si dos números son iguales\n5) Comparar si un número es más grande que el otro\nEscribe el índice: ")
option = int(option)

# El usuario eligió sumar
# Se convierten los números a binarios y despues se suman
if option == 1:
    num1 = int(input("Ingresa el primer número que quieres sumar\nNúmero: "))
    num2 = int(input("Ingresa el segundo número que quieres sumar\nNúmero: "))
    if num1 >= 0:
        arrNum1 = funciones.decimal2BinarioPositive(num1)
    else:
        arrNum1 = funciones.decimal2BinarioNegative(num1)
    
    if num2 >= 0:
        arrNum2 = funciones.decimal2BinarioPositive(num2)
    else:
        arrNum2 = funciones.decimal2BinarioNegative(num2)
    
    sumaBinaria = funciones.binaryAddition(arrNum1, arrNum2)

    print("Overflow: " + str(funciones.detectOverflowInSuma(num1, num2, sumaBinaria)))
    print(sumaBinaria)

# El usuario eligió restar
# Se convierten los números a binarios y después se restan
elif option == 2:
    num1 = int(input("Ingresa el primer número que quieres restar\nNúmero: "))
    num2 = int(input("Ingresa el segundo número que quieres restar\nNúmero: "))
    if num1 >= 0:
        arrNum1 = funciones.decimal2BinarioPositive(num1)
    else:
        arrNum1 = funciones.decimal2BinarioNegative(num1)
    
    if num2 >= 0:
        arrNum2 = funciones.decimal2BinarioPositive(num2)
    else:
        arrNum2 = funciones.decimal2BinarioNegative(num2)
    
    restaBinaria = funciones.binarySubstration(arrNum1, arrNum2)

    print("Overflow: " + str(funciones.detectOverflowInResta(num1, num2, restaBinaria)))
    print(restaBinaria)

# El usuario eligió invertir el número
elif option == 3:
    num = int(input("Ingresa el número para invertir\nNúmero: "))
    if num >= 0:
        num = funciones.decimal2BinarioPositive(num)
    else:
        num = funciones.decimal2BinarioNegative(num)
    print(funciones.complement1(num))

# El usuario eligió comparar si dos números son iguales
elif option == 4:
    num1 = int(input("Ingresa el primer número que quieres comparar\nNúmero: "))
    num2 = int(input("Ingresa el segundo número que quieres comparar\nNúmero: "))
    if num1 >= 0:
        num1 = funciones.decimal2BinarioPositive(num1)
    else:
        num1 = funciones.decimal2BinarioNegative(num1)
    
    if num2 >= 0:
        num2 = funciones.decimal2BinarioPositive(num2)
    else:
        num2 = funciones.decimal2BinarioNegative(num2)
    print(funciones.isEqual(num1, num2))

# El usuario eligió comparar cual de los números es mayor
elif option == 5:
    num1 = int(input("Ingresa el primer número que quieres comparar\nNúmero: "))
    num2 = int(input("Ingresa el segundo número que quieres comparar\nNúmero: "))
    if num1 >= 0:
        num1 = funciones.decimal2BinarioPositive(num1)
    else:
        num1 = funciones.decimal2BinarioNegative(num1)
    
    if num2 >= 0:
        num2 = funciones.decimal2BinarioPositive(num2)
    else:
        num2 = funciones.decimal2BinarioNegative(num2)
    
    print(funciones.mayorMenor(num1, num2))