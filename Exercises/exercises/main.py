

a = [1, 2, 3, 4]
string1 = ''.join(str(i) for i in a)
print(string1)

b = [[1, 2], [3, 4], [5, 6, 7]]
b = [i for j in b for i in j]
print(b)

c = [(0, 2), (1, 1), (2, 5), (3, 3)]
print(sorted(c, key=lambda x: x[1]))

d = [2, 1, 2, 3, 4, 3]
print(list(dict.fromkeys(d)))

# resourcen lead code





