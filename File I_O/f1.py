f = open("demo.txt", "r")
print(f.read())
f.close()
print("1")
f = open("demo.txt", "r")
print(f.read(5))
f.close()
print("2")
f = open("demo.txt", "r")
print(f.readline())
f.close()
print("3")
f = open("demo.txt", "r")
print(f.readline())
print(f.readline())
f.close()
print("4")

f = open("demo.txt", "r")
for x in f:
    print(x)
f.close()  # Don't forget to close the file
print(type(f))



#or
"""
with open("demo.txt", "r") as f:
    for x in f:
        print(x)

"""

