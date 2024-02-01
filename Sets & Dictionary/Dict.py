"""
Dictionary: 

- Dictionaries are used to store data values in key:value pairs
- They are unordered, mutable(changeable) & don't allow duplicate keys

"""

dict = {
    "name": "harpreet",
    "cgpa": 7.88,
    "marks": [88,77,71],
    "age": 19,
    "is_adult": True,
}
print("Dictionary: ", dict)
print(dict["marks"])
print()

dict["name"] = "harjot"
print("Dictionary: ", dict)

print()
#null dictionary
null_dictt = {}
print("Dictionary: ", null_dictt)
print(type(null_dictt))



print()
print()

#Nested Dictionary

student = {
    "name": "Harpreet",
    "score": {
        "chem": 98,
        "phy": 97,
        "math": 95
    }
}

print(student)
#accessing from nested dictionary
print(student["score"]["chem"])  #98



#.........................................................................

#METHODS: 

#  1. It returns all keys
keyy = student.keys()
# or list(student.keys()) 
print(keyy)
# dict_keys(['name', 'score'])


#  2. returns all values
vall = student.values()
print(vall)
#dict_values(['Harpreet', {'chem': 98, 'phy': 97, 'math': 95}])


#  3. returns all key, value pairs from dictionary as tuples
keyyVal = student.items()
print(keyyVal)

#dict_items([('name', 'Harpreet'), ('score', {'chem': 98, 'phy': 97, 'math': 95})])


#  4. retiurns the key acc to value
keyt = student.get("name")
print(keyt)

#  5. update

up = student.update({"city": "Chandigarh"})
print(student)