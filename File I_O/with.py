with open("with_data.txt", "r") as f:
    data = f.read()
    print(data)

# with open("with_data.txt", "w") as f:
#     f.write("Hello")
#     f.close()  # This is not necessary, 'with' statement will close the file for you

