#ANDREW PANG
#5 APRIL 2019
#TASK 1

usr_in = input("Enter file name (eg.'Tiny.txt') :")

#opens reads and tidies up the file
#creates a new list containing data 
z = open(usr_in,'r')
z = z.read()
z = z.strip()
z = z.split('\n')

newz = []

#runs thru every line in list z
#adds the datum to newz
for i in z :
    newrow = i.split(',')
    newrow[0] = int(newrow[0])
    newrow[1] = float(newrow[1])
    newz.append(newrow)



def print_list(fdata):
    
    for i in fdata:
        print( str(i[0]) + ' kms, $' + str(i[1]))
        
    return None

print_list(newz)
