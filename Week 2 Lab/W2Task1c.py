#Name : Andrew Pang
#Date : 8 Mar 2019
#Task 1(a&b)  

import random #imports random module

#retrieves no. of coin flips from user
y = int(input("Enter number of coin flips (eg. 15) : ")) 

#variables
result = ''

#cumulative counters
i = 0 
j = 0
k = 0

#runs the code for y number of times (no. of coin flips)
for z in range (1,y + 1) :

    #generates a random number from 1 to 3
    fl = random.randrange(1,4)

    #if else loop to add the number of sides to the cumulative counter
    if fl == 1:
        i += 1

    elif fl == 2:
        j += 1

    else :
        k += 1
        
    #prints the results for each coin flip
    print(" Coin flip " + str(z) + " ends up on side " + str(fl)) 


#more info on all the coin flips (for verification purpose)
print( "Total side 1 : " + str(i)) 
print( "Total side 2 : " + str(j))
print( "Total side 3 : " + str(k))
print( "Ratio of side 1 : " + str(i/y))
print( "Ratio of side 2 : " + str(j/y))
print('Ratio of side 3 : ' + str(k/y))
