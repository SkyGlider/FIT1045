#ANDREW PANG
#19 MAR 2019
#TASK 5

#imports random module
import random

#create empty list dice_result
dice_result = []

#for loop i that runs from 0 to 999
for i in range(1000) :
    
    #generate random number form 1 to 6
    side = random.randrange(1,7)

    #adds the result to the list
    dice_result.append(side)

#cumulative counter     
side_sum = 0

#runs through every element in dice_result
for y in dice_result :
      side_sum += y

#finds the average
avg = side_sum/(len(dice_result))

print('The average score is : ' + str(avg))
    
