"""
WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
an empty dictionary & add one by one. Use subject name as key & marks as value.

"""
dict = {}

sub1 = input("Enter Maths: ")
dict.update({"Maths": sub1})


sub2 = input("Enter chem: ")
dict.update({"Chem":sub2})


sub3 = input("Enter phy: ")
dict.update( {"Phy" :sub3})



print(dict)
