import random

x = float(input("Enter your bias for heads (eg.0.4) : "))
y = int(input("Enter number of coin flips (eg. 15) : "))
result = True
i = 0
j = 0
for z in range (1,y + 1) :
    if random.random() > x :
        result = False
        i += 1       
    else :
        result = True
        j += 1
    print(" Coin flip " + str(z) + " returns heads : " + str(result))
z += 1

print( "Total heads : " + str(j) )
print( "Total tails : " + str(i))
print( "Percentage of heads : " + str(j*100/y) + "%")

    
        


