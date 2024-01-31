"""
A built-in data type that stores set of values
It can store elements of different types (integer, float, string, etc.)


-> Strings are Immutable in Python
-> Lists are Mutable in Python

"""

marks = [94.4,87,66,33,95,76]
print(type(marks))  # <class 'list'>
print(marks)

print('\n')

print(marks[3])

print('\n')

print("length of list : ", len(marks))

print('\n')

data1 = ["hs", 95, "51", "dhcb"]
print(type(data1)) # <class '

print('\n')

data1[0] = "harjot"
print(data1)

print('\n')

#Slicing - same rules like in Strings

marks = [85,69,45,98,48,94]
print('Full Marks: ', marks)
print('Marks from index 2 to end: ', marks[2:])
print('Marks from start to index 3: ', marks[:3])
print('negative slicing: ', marks[-3 : -1])

print('\n')


