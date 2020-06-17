lucky_numbers = [42, 83, 12, 15, 16, 3, 2]

friends = ["Kevin", "Karen", "Jim", "Oscar", "Tim"]
print(friends)

#adds a list to another
#friends.extend(lucky_numbers) 

#appends an item to the end of a list
friends.append("Creed")
print(friends)

#insert a value at the index(first value), pushing all other items one place to the right(index)
friends.insert(1, "Sophie")
print(friends)

#remove the element passed to the function
friends.remove("Kevin")
print(friends)

#remove last element in the list
friends.pop()
print(friends)

#look for certain value in list
print("Oscar is at index " + str(friends.index("Oscar")))

#we can also sort lists in ascending order
friends.sort()
print(friends)

 