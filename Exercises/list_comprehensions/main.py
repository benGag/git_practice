
# new list with items of fruits containing letter a 
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist_a = [x for x in fruits if "a" in x]

""" equivalent to: 

for x in fruits:
  if "a" in x:
    newlist_a.append(x)

syntax:
newlist = [expression for item in iterable if condition == True]

"""

newlist_n = [i for i in fruits if "n" in i]

print(newlist_a)
print(newlist_n)


# creating list of 4 elements with a list comprehension
newlist_1 = [x for x in range(4)]
print(newlist_1)


# manipulating the expression before adding to list 
print([x.upper() for x in fruits])

#further manipulation
print([x if x != 'banana' else 'orange' for x in fruits])




#flatting list with list comprehension
nested_list = [[1,2], [3,4], [4,5]]
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)


# string to list of characters 
name = "Benedikt"
print([x for x in name])







