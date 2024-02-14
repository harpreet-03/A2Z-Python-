def calSum(n):
    if n == 1:
        return 1
    else:
        return n + calSum(n-1)
    
sum = calSum(5)
print("Sum: ", sum)