#String is data type that stores a sequence of characters.

str1 = "string"
print(type(str1))  # Output: <class 'str'>
print()
#concatenation
str2 = "is"
str3 = str1 +" "+ str2
print(str3)     #Output: string is
print()

#length
len_of_str = len(str3)
print("Length of the string :", len_of_str)   #Output: Length>
print()

#indexing
print("Index of the string str[0]:", str3[1])


#Slicing: Accessing parts of a string
# ------------------------------------------------------------------------
# str[starting_index, ending_index(not inclusive)]
print()

str4 = str3[1:4]
print("Sliced part of the string str4[1:4]: ",str4)
print()

#str4[:4] -> str4[0 : 4]
#str4 [5:] -> str5[5: len(str)]
str5 = "Harpreet Singh"
print("Sliced part of the string str4[5:] :", str5[5: ])
print()


#Negative Slicing

s = "Apple"
str = s[-3: -1]
print(str)
#Output: pl
#same logic: ending index will not inclusive


# ----------------------------------------------------------------------------------



