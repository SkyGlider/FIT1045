#ANDREW PANG
#5 APRIL 2019
#TASK 4
import math

def selectionSortDistance(fdata):
    
    #runs thru every element in the list EXCEPT the last
    for i in range(len(fdata)-1):
        hold = fdata[i][0]
        minval = math.inf
        
        #runs thru every element in the list AFTER the selected index
        for j in range(i+1,len(fdata)):
            if fdata[j][0] < minval:
                minval = fdata[j][0]
                mindex = j
                
        #swaps the value in current index with the minimum value found
        if hold > minval :
            fdata[i] , fdata[mindex] = fdata[mindex] ,fdata[i]
 
    return fdata


def selectionSortPrice(fdata):

    #runs thru every element in the list EXCEPT the last
    for i in range(len(fdata)-1):
        hold = fdata[i][1]
        minval = math.inf

        #runs thru every element in the list AFTER the selected index
        for j in range(i+1,len(fdata)):
            if fdata[j][1] < minval:
                minval = fdata[j][1]
                mindex = j

        #swaps the value in current index with the minimum value found
        if hold > minval :
            fdata[i] , fdata[mindex] = fdata[mindex] ,fdata[i]

    return fdata
    
            
def print_list(fdata):
    
    for i in fdata:
        print( str(i[0]) + ' kms, $' + str(i[1]))
        
    return None

#main code
usr_in = input("Enter file name (eg.'Tiny.txt') :")

#open reads and puts the data into a new list
z = open(usr_in,'r')
z = z.read()
z = z.strip()
z = z.split('\n')

newz = []

for i in z :
    newrow = i.split(',')
    newrow[0] = int(newrow[0])
    newrow[1] = float(newrow[1])
    newz.append(newrow)
    
currentlist = newz

#while loop until user quits
while True:
    usr_ch = input("Enter 'print', 'sort1' (distance) , 'sort2' (price) or 'quit' :")

    if usr_ch.lower() == 'quit':
        print("Thank You for using Andrew's Price/Distance selector!")
        break
    elif usr_ch.lower() == 'sort1':
        currentlist = selectionSortDistance(currentlist)
    elif usr_ch.lower() == 'sort2':
        currentlist = selectionSortPrice(currentlist)
    else:
        print_list(currentlist)
