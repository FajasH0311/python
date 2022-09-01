numbers = [5, 2, 1, 5, 7, 4]
numbers.append(20) ##this adds the number in bracket at the end of the list
numbers.insert(0, 10) ## using insert adds the number in wherever position u need in this 0 is the position 10 is the number you need to add
numbers.remove(5) ## this removes the item mentioned from list
numbers.clear() ## this clears the whole list
numbers.pop() ## removes the last item in the list
print(numbers.index(7)) ## this states the index/postion of the number mentioned
print(50 in number) ## this is much safer to use than .index bcs this will give boolean statement if there isnt the no that mentioned other than a error
numbers.count(5) ## this counts no of times the mentioned no appears in the list
numbers.sort() ## this will arrange the list in ass.order
numbers.reverse() ## this will be in des.order
numbers2 = numbers.copy() ## this will copy the list so that even we mess the 1st 2nd will not get messed up
print(numbers)