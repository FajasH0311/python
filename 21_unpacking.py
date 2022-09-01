coordinates = (1, 2, 3) ## (x, y, z)
coordinates[0] * coordinates[1] * coordinates[2] ##positons are the values in sqr bracket

## easy method than repeating this is to mention them as variables
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

x * y * z ## this is easy

## but unpacking is the easiest
x, y, z = coordinates ## this method also works with lists
## in this we are giving the name to their index so even if it is sqr brkt this works

print(x)