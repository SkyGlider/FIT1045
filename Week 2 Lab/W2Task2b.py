#Name : Andrew Pang
#Date : 8 Mar 2019
#Task 2c

#prompts the user to input desired start and end values and convert them to integers
start_pt = int(input("Enter Start Number : "))
end_pt = int(input("Enter Last Number : "))

#define a cumulative counter
i = 0

#calculates the value of 3z for every value between start and end values
for z in range(start_pt,end_pt+1) :
  output = 3*z
  i = i + output
   
#prints the result
print("The result for sum 3i from " + str(start_pt) + " to " + str(end_pt) + " is "+ str(i))

