def toDecimal(nums):
    finDec = 0
    for i in range(len(nums)):
        print(2**0)
        if nums[i] == 1:
            finDec += 2**i
        else:
            continue

    return finDec

print(toDecimal([1,1,1,1]))