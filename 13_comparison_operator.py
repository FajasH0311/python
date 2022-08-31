## if name is less than 3 characters long
## name must be at least 3 characters
## otherwise if it's more than 50 characters long
## name can be a maximum of 50 characters
## otherwise
## name looks good !

name = input("What is your name? ")
name_len = len(name)

if name_len < 3:
    print("name should be atleast 3 letters")
elif name_len > 50:
    print("Name should be less than 50 words")
else:
    print("Name looks good")