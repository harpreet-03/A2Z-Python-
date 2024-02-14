def factoriall(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
    
factt = factoriall(5)


# using recursion
def fact(n):
    if(n == 0):
        return 1 
    
    return n * fact(n-1)

fact(5)