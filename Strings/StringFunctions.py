str = "i am a Coder."

print(str.endswith("er.") )   #returns true if string ends with substr

print(str.capitalize()  )   #capitalizes 1st char

print(str.replace("a","@"))    #replaces all occurrences of old with new


print(str.find("a")    ) ##returns 1st index of 1st occurrence

print(str.count("d") )##counts the occurrences od substr in a string

"""
output: 

True
I am a coder.
i @m @ Coder.
2
1

"""