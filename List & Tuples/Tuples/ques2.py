# WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)

org = [1, 2, 3, 2, 1]
rev = org.copy()  # Use copy() to create a copy of the original list
rev.reverse()

if org == rev:
    print("true")
else:
    print("no")
