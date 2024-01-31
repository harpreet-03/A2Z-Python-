#A built-in data type that lets us create immutable sequences of values.

#we use ( ) parenthesis to create tuple

#in list; we use Square bracket []
#Tuples are immutable, meaning their value cannot be changed after they have been created.
#They can only be updated or added to, but they cannot be removed or altered in place
#We can access the elements using indexing like lists

t = ("apple", "banana", "cherry")  
print(type(t))   #<class 'tuple'>
print(t)
#output: ('apple', 'banana', 'cherry')

#assignment is not allowed in tuples



"""
if we're declaring only one element in the tuple:

we use , or comma immediatley after the first element
eg:

tup = (1,)
print(type(tup)) <class 'tuple'>



----> 
if we don't use the  comma, then what would happen is that python will consider it as a normal integer written int the brackets, so returns the type: Integer...

"""
tup  = (1)
print(type(tup)) 
#<class 'int'>

print('\n')

tup1 = ("hello")
print(type(tup1))
#<class 'str'>

print('\n')

tup3 = (1,)
print(type(tup3))
#<class 'tuple'>

# ---------------------------------------------------------

# Methods

tupp = (2,1,3,1)

print(tupp.index(2)) #returns the index of 1st occurences
# 0

print(tupp.count(1)) #returns the total occurences
# 2
