#ANDREW PANG
#5 APRIL 2019
#TASK 2
import math

usr_in = input("Enter file name (eg.'Tiny.txt') :")

#opens reads and tidies up the file
#creates a new list containing data 
z = open(usr_in,'r')
z = z.read()
print(z)
z = z.strip()
z = z.split('\n')

newz = []

for i in z :
    newrow = i.split(',')
    newrow[0] = int(newrow[0])
    newrow[1] = float(newrow[1])
    newz.append(newrow)

def selectionSortDistance(fdata):
    
    #runs thru every item in list fdata
    for i in range(len(fdata)-1):
        hold = fdata[i][0]
        minval = math.inf
        for j in range(i+1,len(fdata)):
            if fdata[j][0] < minval:
                minval = fdata[j][0]
                mindex = j
        
        if hold > minval :
            fdata[i] , fdata[mindex] = fdata[mindex] ,fdata[i]

    
    return fdata
            

def print_list(fdata):
    
    for i in fdata:
        print( str(i[0]) + ' kms, $' + str(i[1]))
        
    return None

print_list(selectionSortDistance(newz))
