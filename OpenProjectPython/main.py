with open("emails.csv", 'r') as f:
    rawData = f.read()

h = rawData[:358]
print(h)
data = rawData[358:]

rows = data.split('"""";;;;;;;')
print("#########ROW1", rows[0][:50])
print("#########ROW2", rows[1][:50])
print("#########ROW3", rows[2][:50])
print("#########ROW4", rows[3][:50])
print("#########ROW5", rows[4][:50])
