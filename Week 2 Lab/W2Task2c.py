#Name : Andrew Pang
#Date : 8 Mar 2019
#Task 2c

#prompts the user to enter desired start and end values and converts to int.
start_pt = int(input("Enter Start Number : "))
end_pt = int(input("Enter Last Number : "))

#prompts the user for divisible value and converts to int.
div_val = int(input("Only consider values divisible by : "))

#i is a cumulative counter
i = 0

#runs through every value between the start and end values inclusive
for z in range(start_pt,end_pt+1) :

   #ensures the value is specifically divisible by div_val, checked by z % div_val
   if (z % div_val) == 0 :

      #performs the operation to values that meet the requirement
      output = 2*(z**2) + 4*z
      i = i + output
   
#prints the result
print("The result for sum 2i^2 + 4i from " + str(start_pt) + " to " + str(end_pt) + " is "+ str(i))
