import math
x = int(input("Enter x value : "))
n = int(input("Enter n value : "))

lga = (math.log(x,math.e))/n
a = math.exp(lga)

print("The " + str(n) + " root of " + str(x) + " is " + str(a))
