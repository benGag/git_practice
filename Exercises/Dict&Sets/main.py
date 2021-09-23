thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#print(thisdict)

# ordered since v3.7
# unordered lower than v3.7
# mutable and dynamic
# can be nested


thisSet = {"apple", "banana", "cherry"}
#print(thisset)

# unordered
# keine duplicates, unique
# A set itself may be modified, but the elements contained in the set must be of an immutable type.

program = "progra"

myDict = {
  program : "JumpStart",
  "track" : "data",
  "members" : ["Michael", "Jonas", "Sophie", "Rosa", "Kismet", "Ben"],
  "training" : ["python", "big_data", "ai", "talend"]
}

#print(myDict)





my_dict = {"a": 1, "b": 2, "c": 3}

for x in my_dict.keys():
  my_dict[x] += 1

print(my_dict)


# effizienterer weg
new_dict = {key: value+1 for key, value in my_dict.items()}

print(new_dict)






































