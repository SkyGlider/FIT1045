a_list = [ None for i in range(5)]

count  = 0
while count < 5:
    a_list[count] = count
    count = count + 1

print(a_list)
