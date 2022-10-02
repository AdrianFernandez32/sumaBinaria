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
    pot = 16
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
    binaryNum = decimal2BinarioPositive(num)
    i = 0
    for i in range(len(binaryNum)):
        if binaryNum[i] == 1:
            binaryNum[i] = 0
        else:
            binaryNum[i] = 1
    binaryNum[-1] = 1
    return binaryNum

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
    
    reverse(newNumber)
    return newNumber

num1 = [1,0,0,1,1,1,0,1,1]
num2 = [0,1,1,1,0,0,1,0,1]

print(binarySubstration(num1, num2))