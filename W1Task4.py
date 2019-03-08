#Name : Andrew Pang, Teng Sin Hui
#Date : 8 Mar 2019
#Task 2 : Numerical Operations

x = int(input("Enter x value : ")) #Retrieves user input for x value and converts to integer
n = int(input("Enter n value : ")) #Same for n value

lga = (math.log(x,math.e))/n #calculates log(a)
a = math.exp(lga) #calculates (a)

print("The " + str(n) + " root of " + str(x) + " is " + str(a)) #prints the answer 
