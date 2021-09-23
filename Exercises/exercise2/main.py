full_name = input("Please enter first and last name separated by space: ")
x = full_name.split()

new_name = " ".join([y[::-1] for y in x])

print(new_name)




#for i in range(len(x)):
#    new_name += (x[i][::-1]) + " "

