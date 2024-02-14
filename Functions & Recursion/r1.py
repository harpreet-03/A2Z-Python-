#prints n to 1 backwards

def show(n):
    if n==0:    #base case (stopping condition)
        return
    print(n)
    show(n-1)

show(10)

"""
output: -> 

10
9
8
7
6
5
4
3
2
1

"""

