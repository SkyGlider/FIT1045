#Name : Andrew Pang
#Date : 8 Mar 2019
#Task 2d

#input start and end numbers from user
i = int(input("Enter Start Number : "))
n = int(input("Enter Last Number : "))

#define cumulative counter x to be zero
x = 0

#for loop for value y, and value z within for loop y
for y in range(i,n+1) :               
   
   for z in range(1,y+1) :             
 
      output = 2*(y**2) + 4*(z)        #note: 2*(the previous number in y)^2 + 2*(current number of z)    
      x = x + output                   
  
#prints the result
print("The result for sum of sum 2i^2 + 4i from " + str(i) + " to " + str(n) + " is "+ str(x))
