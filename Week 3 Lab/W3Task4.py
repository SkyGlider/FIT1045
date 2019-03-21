#ANDREW PANG
#19 MAR 2019
#TASK 4

my_list = []

for i in range(5):
    usr_in = input('Enter Some Numbers: ')
    usr_list = usr_in.split(' ')
    
    y = [int(y) for y in usr_list]
    
    my_list.append(y)
    
print(my_list)
