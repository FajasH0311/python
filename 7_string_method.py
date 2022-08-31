name = 'Syed Farhan'

print(len(name))
print(name.upper())
print('Syed' in name)
print('syed' in name)
print('syed' in name.lower())

## len - is used to find how many letter are in the variable
## var.upper() - this makes every letter in the string to upper case
## var.lower() - this makes everything to lower 

## var.find('## the postion of letter you need to find ##')
## var.find('## letter not in the variable ##') - this will print -1
## var.find('## if you give a word ##') - it prints the postion at which the words first letter begins

## var.replace('## the word or letter you need to replace ##', '## the word you need to replace it with ##')

## print('## a word or letter to check ##' in var) -- to check the word or letter in the var if yes print True