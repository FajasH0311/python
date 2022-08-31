from email import message_from_binary_file


first = 'John'
last = 'Smith'
message = first + '[' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'
print(message)
print(msg)


## var = f''  --- this is a formatted string
## var = f'{first} is a coder'
## in the above {} -- in this we add the name of variable
## there by we don't have to use + btween each str and easy to look
