#Name : Andrew Pang
#Date : 8 Mar 2019
#Task 1(a&b)  

import random #imports random module

#retrieves bias from user
x = float(input("Enter your bias for heads (eg.0.4) : "))
#retrieves no. of coin flips from user
y = int(input("Enter number of coin flips (eg. 15) : ")) 

#variables
result = True

#cumulative counters
i = 0 
j = 0

#runs the code for y number of times (no. of coin flips)
for z in range (1,y + 1) :
    
    #gives a 'True' result if its a heads and vice versa
    #if random generated number is less than the bias, it is a heads
    if random.random() > x : 
        result = False
        i += 1       
    else :
        result = True
        j += 1
        
    #prints the results for each coin flip
    print(" Coin flip " + str(z) + " returns heads : " + str(result)) 


#more info on all the coin flips (for verification purpose)
print( "Total heads : " + str(j)) 
print( "Total tails : " + str(i))
print( "Ratio of heads : " + str(j/y))
print( "Ratio of tails : " + str(i/y))
