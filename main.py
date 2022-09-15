import collections
##############################################################################################
# Whole functions, just that
##############################################################################################

def toBinary(num):
    q = collections.deque()
    
    i = 0
    while num > 1:
        if num%2 == 1:
            q.append(1)
        else:
            q.append(0)
        num = num//2
    
    if num == 2:
        q.append(0)
    elif num == 1:
        q.append(1)
    else:
        q.append(0)
    
    while len(q) < 16:
        q.append(0)
    
    return q

def reverse(q):
    i = 0
    j = len(q)-1
    while i < j:
        q[i], q[j] = q[j], q[i]
        i += 1
        j -= 1
    return q

def binaryAddition(arr1, arr2):
    newNumber = []
    carry = 0
    for i in range(len(arr1)):
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
    if carry == 1:
        overflow = True
    else:
        overflow = False
    
    return newNumber

def toDecimal(nums):
    finDec = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            finDec += 2**i

    return finDec

def hasOverflow(overflow, finalNumbers):
    if overflow == True:
        finalNumbers.pop()
    print("Overflow: " + str(overflow))
    
    return finalNumbers

# Path step-by-step

numA = int(input("Pon un decimal que quieras sumar: "))
numB = int(input("Pon otro decimal que te gustaría sumar: "))
sumDec = numA + numB
overflow = False

binaryA = toBinary(numA)
binaryB = toBinary(numB)
binarySum = binaryAddition(binaryA, binaryB)
binaryNumberwError = hasOverflow(overflow, binarySum)

print("------------------------------------------------------")
print("El primer número es: " + str(reverse(binaryA)))
print("El segundo número es: " + str(reverse(binaryB)))
print("-------------------------------------------------------")
print("La suma decimal de los números es: " + str(sumDec))
print("La suma binaria es: " + str(reverse(binarySum)))
print("-----------------------------------------------------")
reverse(binaryNumberwError)
print("El numero final en decimal es: " + str(toDecimal(binaryNumberwError)))
print("El overflow y el numero binario: " + str(reverse(hasOverflow(overflow, binaryNumberwError))))
