#Name : Andrew Pang
#Date : 8 Mar 2019
#Task 5

#imports random module
import random 

#retrieves bias from user
x = float(input("Enter your bias for heads (eg.0.4) : "))


#variables
result = True 

#runs the code for y number of times (no. of coin flips)
for z in range (1,11) :
    
    #gives a 'True' result if its a heads and vice versa
    #in this case, if the random number generated is is less that the bias, it is a heads
    if random.random() < x :
        
        result = True
          
    else :
        
        result = False

    #prints the results for each coin flip
    print(" Coin flip " + str(z) + " gives heads : " + str(result)) 




    
        


