#ANDREW PANG
#29/3/2019
#TASK 2


import math

'''opens, reads and imports data of the file'''
z = open('Tides.txt','r')
z = z.read()
z = z.replace(' meters','')
z = z.split('\n')

#PART A
'''splits every row into a list and convert string data to float'''
newlist = []
for i in z :
    newrow = i.split(',')
    newrow[1] = float(newrow[1])
    newrow[2] = float(newrow[2])
    newlist.append(newrow)

#print(newlist)

#PART B
'''checks the current date
if it is same with previus date, max/min val not overwritten
else, it is overwritten and (set to 0 and inf)'''
lastday = newlist[0][0]
max_val = 0
min_val = math.inf
for i in newlist :
    currentday = i[0]
    if not lastday == currentday :
        #print( lastday + ' : ' + str(min_val) + ' meters at low, ' + str(max_val) + ' meters at high')
        max_val = 0
        min_val = math.inf
            
    if i[2] > max_val :
        max_val = i[2]
            
    if i[2] < min_val:
        min_val = i[2]
        
    lastday = currentday

'''prints the last row'''
#print( lastday + ' : ' + str(min_val) + ' meters at low, ' + str(max_val) + ' meters at high')



#PART C
'''use newlist to create timelist, with times of max and min'''
lastday = newlist[0][0]
max_val = 0
min_val = math.inf
timelist = []

for i in newlist :
    currentday = i[0]
    
    if not lastday == currentday :
        newrow = [ lastday , min_time, min_val, max_time, max_val ]
        #print(newrow)
        timelist.append(newrow)
        max_val = 0
        min_val = math.inf
            
    if i[2] > max_val :
        max_val = i[2]
        max_time = i[1]
            
    if i[2] < min_val:
        min_val = i[2]
        min_time = i[1]
        
    lastday = currentday

'''for the last row'''
newrow = [ lastday , min_time, min_val, max_time, max_val ]
#print(newrow)
timelist.append(newrow)

'''calculates the sum of every high and low tide times'''
'''calculates the average time'''
low_sum = 0
high_sum = 0
for i in timelist:
       low_sum += i[1]
       high_sum += i[3]

high_avg = high_sum/len(timelist)
low_avg = low_sum/len(timelist)

print('Over the full period,')
print('Average lowest tides occurred at '+ str(low_avg) + ' hours after midnight' )
print('Average highest tides occurred at '+ str(high_avg) + ' hours after midnight')
        
        
    
    
    

        
