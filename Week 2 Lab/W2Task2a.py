#Name : Andrew Pang
#Date : 8 Mar 2019
#Task 2a

#cumulative counter i
i = 0

#for loop that runs through all the values from 1 to 10
for z in range(1,11) :

    #carries out operation for each value of z
    output = 3*z
    #adds the output to i cumulatively
    i = i + output
    
#prints the result
print("The result for sum 3i for i from 1 to 10 is " + str(i))
