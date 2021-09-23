old_list = list(range(1,11))
new_list = old_list.copy()

for x in range(0, len(new_list)):
    new_list[x] += 1

print(old_list)
print(new_list)

# very efficient way with list comprehensions

new_list2 = [x+1 for x in old_list]
print(new_list2)

