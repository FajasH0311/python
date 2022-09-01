## to remove the duplicates in the list

from enum import unique


numbers = [2, 2, 4, 3, 5, 5, 8, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)