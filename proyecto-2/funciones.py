# Primero que nada crearemos funciones básicas

# Función para invertir un array
# e.g.
# [0,1,1,0,1,0] -> [0,1,0,1,1,0]
def reverse(nums):
    i = 0
    j = len(nums)-1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    return nums

# Función para pasar un número positivo decimal a binario
# e.g.
# 355 -> 101100011
def decimal2BinarioPositive(num):
    num = abs(num)
    binaryNum = []
    pot = 15
    while pot >= 0:
        if num >= 2**pot:
            binaryNum.append(1)
            num -= 2**pot
        else:
            binaryNum.append(0)
        pot -= 1
    return binaryNum

# Función para pasar un número negativo decimal a binario
# e.g.
# -355 -> 010011101
def decimal2BinarioNegative(num):
    binaryComplement = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
    binaryNum = decimal2BinarioPositive(num)
    i = 0
    for i in range(len(binaryNum)):
        if binaryNum[i] == 1:
            binaryNum[i] = 0
        else:
            binaryNum[i] = 1
    binaryNum = binaryComplementoA2(binaryNum, binaryComplement)
    

    return binaryNum

# Función para sumar el último bit en complemento a 2
def binaryComplementoA2(arr1, arr2):
    newNumber = []
    carry = 0
    i = len(arr1)-1
    while i >= 0:
        if arr1[i] == 0 and arr2[i] == 0:
            newNumber.append(0 + carry)
            carry = 0
        elif arr1[i] == 1 and arr2[i] == 1:
            if carry == 1:
                newNumber.append(1)
            else:
                newNumber.append(0)
                carry = 1
        else:
            if carry == 1:
                newNumber.append(0)
            else:
                newNumber.append(1)
                carry = 0
        i -= 1
    if carry == 1:
        newNumber.append(1)
    reverse(newNumber)
    return newNumber

# Función para sumar dos números binarios
# e.g.
# 101100011 + 11010010 = 1000110101
def binaryAddition(arr1, arr2):
    newNumber = []
    carry = 0
    i = len(arr1)-1
    while i >= 0:
        if arr1[i] == 0 and arr2[i] == 0:
            newNumber.append(0 + carry)
            carry = 0
        elif arr1[i] == 1 and arr2[i] == 1:
            if carry == 1:
                newNumber.append(1)
            else:
                newNumber.append(0)
                carry = 1
        else:
            if carry == 1:
                newNumber.append(0)
            else:
                newNumber.append(1)
                carry = 0
        i -= 1
    if carry == 1:
        newNumber.append(1)
    
    print("Tiene overflow: "+ str(detectOverflow(newNumber)))
    reverse(newNumber)
    return newNumber

# Función para restar dos números binarios
# arr1 es el superior y arr2 es el inferior
# e.g.
# 101100011 - 11010010 = 10010001
def binarySubstration(arr1, arr2):
    newNumber = []
    carry = 0
    i = len(arr1)-1
    while i >= 0:
        if arr1[i] == 0 and arr2[i] == 1:
            if carry == 1:
                newNumber.append(0)
            else:
                newNumber.append(1)
                carry = 1
        elif arr1[i] == 0 and arr2[i] == 0:
            if carry == 1:
                newNumber.append(1)
            else:
                newNumber.append(0)
        elif arr1[i] == 1 and arr2[i] == 1:
            if carry == 1:
                newNumber.append(1)
            else:
                newNumber.append(0)
        else:
            if carry == 1:
                newNumber.append(0)
                carry = 0
            else:
                newNumber.append(1)
        i -= 1
    print("Tiene overflow: "+ str(detectOverflow(newNumber)))
    reverse(newNumber)
    return newNumber

# Función para detectar overflow (Si es mas largo que 16 bits, se detecta el overflow)
def detectOverflow(nums):
    if len(nums) > 16:
        return True
    else:
        return False

# Comparar si un número es más grande que otro e indicar cual es más grande
# e.g.
# 101100011 - 101010010 = 101100011
def mayorMenor(arr1, arr2):
    arr = binarySubstration(arr1, arr2)
    if arr[0] == 1:
        mayor = arr2
        return arr2
    else:
        mayor = arr1
        return mayor

# Funcion para comparar si dos números son iguales
# e.g.
# 1001 == 1001 = True
def isEqual(arr1, arr2):
    arr = binarySubstration(arr1, arr2)
    for i in range(len(arr)):
        if arr[i] != 0:
            return False
    return True

# Función para invertir el número dado
# e.g.
# 1001 -> 0110
def complement1(nums):
    i = 0
    while i < len(nums):
        if nums[i] == 1:
            nums[i] = 0
        else:
            nums[i] = 1
        i += 1
    return nums
