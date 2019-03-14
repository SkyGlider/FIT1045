#Name : Andrew Pang, Teng Sin Hui
#Date : 8 Mar 2019
#Task 5 

import random #imports random module

x = float(input("Enter your bias for heads (eg.0.4) : ")) #retrieves bias from user
y = int(input("Enter number of coin flips (eg. 15) : ")) #retrieves no. of coin flips from user

#parameters
result = True 
i = 0 
j = 0

#runs the code for y number of times (no. of coin flips)
for z in range (1,y + 1) :
    #gives a 'True' result if its a heads and vice versa
    if random.random() > x : 
        result = False
        i += 1       
    else :
        result = True
        j += 1
    print(" Coin flip " + str(z) + " returns heads : " + str(result)) #prints the results for each coin flip
z += 1

#more info on all the coin flips (for verification purpose)
print( "Total heads : " + str(j)) 
print( "Total tails : " + str(i))
print( "Percentage of heads : " + str(j*100/y) + "%")

    
        


