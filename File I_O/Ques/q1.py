"""
Create a new file "practice.txt" using python. Add the following data in it:

Hi everyone
we are learning File I/O
using Java.
like programming in Java.

WAF that replace all occurrences of •java" with -python" in above tile.

Search if the word "leanring" exist in the file or not.

"""






"""
with open("q1.txt", "a") as f:
    f.write("Hi everyone\nwe are learning File I/O \nusing Java \nlike programming in Java.")
    f.close()

    
output: 

Hi everyone
we are learning File I/O 
using Java 
like programming in Java.

"""

#replacing java with Python

# with open("q1.txt", "r") as f:
#    data = f.read()

# new_data = data.replace("Java", "Python")

# print(new_data)

# with open("q1.txt", "w") as f:
#    f.write(new_data)



# #fucntion for searching "learning"

# def check_for_word():
#    with open("q1.txt", "r") as f:
#     data = f.read()
#     if "learning" in data:
#         print("Yes")
#     else:
#         print("No")

# check_for_word()

# #output: Yes


#check for line :

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("q1.txt", "r") as f:
        while data:
            data = f.readline()
            if word in data:
                print("Line No:", line_no)
                return
            line_no += 1

    return -1

check_for_line()

#output: Line No: 2

   
