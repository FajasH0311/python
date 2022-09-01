matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[0][1] = 20 ## you can edit the value inside matrix like this
print(matrix[0][1]) ## 1st square bracket represents the row 2nd the position in that row in this case 1st line position of 2

for row in matrix:
    for item in row:
        print(item) ## this will print the items in the matrix
        