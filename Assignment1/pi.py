#ANDREW PANG YONG CHEN 30506271
#FIT1045
#STARTED : 16 MAR 2019
#COMPLETED : 17 MAR 2019
#SUBMITTED : 4 APR 2019
#ASSGNMENT 1 TASK 1 : PI

import math

#basel function
def basel(precision) :
    
    #initial pi value & number of terms
    calc_pi = 0
    n  = 0

    
    while abs( calc_pi - math.pi) > precision :

            #counts number of terms, if the previous no. is inadequate
            n +=1
            
            #initial sum of terms is 0
            term_sum = 0

            #for loop to calculate each term and add to termsum value
            for i in range (1,n+1) :
                
                term_sum += 1/(i**2)

            #gets the calculated value of pi
            calc_pi = math.sqrt(term_sum*6)
            

    return calc_pi , n
            
#taylor function
def taylor(precision) :

    #initial pi value & number of terms
    n = 0
    calc_pi = 0
    
    while abs( calc_pi - math.pi ) > precision :
            
            n += 1
            term_sum = 0
            
            #seperate variable for denominator value counter
            nums_counter = 1
            
            for i in range(1,n+1):

                    #if its an odd term (eg, 1st,3rd,..), it adds itself
                    #if its an even term (2nd, 4th,..), it subtracts iteslf
                    if i % 2 == 0 :
                        term_sum -= (1/nums_counter)
                    else :
                        term_sum += (1/nums_counter)
                    
                    #the denominator of succesive terms increases by 2
                    nums_counter += 2
                    
            
            #gets the calcuated value of pi
            calc_pi = 4*term_sum
            
            
    return calc_pi , n


#wallis function
def wallis(precision) :

    #initial value of pi and term counter
    calc_pi = 0
    n = 0

    while abs( calc_pi - math.pi ) > precision :
        
        n += 1

        #seperate counters for numerator and denominators
        top_counter = 2
        bot_counter_1 = 1

        #since its a multiplication series, the term sum is at 1 instead of 0
        term_sum = 1
        
        for i in range(1,n+1) :

            term_sum = term_sum*((top_counter**2)/(bot_counter_1*(bot_counter_1+2)))

            #both numerator and denominator values increases by 2 per iteration
            top_counter += 2
            bot_counter_1 += 2

        #gets the calculated value of pi
        calc_pi = 2*term_sum

        
    return calc_pi , n


#spigot function
def spigot(precision):

    #initial value of pi and terms counter
    calc_pi = 0
    n = 0

    while abs( calc_pi - math.pi ) > precision :

        #seperate counters for numerator and denominators
        top_counter = 1
        bot_counter = 3
        
        #we start with a value of 1, for simplification purposes
        term_sum = 1
        
        #since each term requires more multiplication with every increaing term,
        #a variable is given for each term
        each_term = 1

        #this loop doesnt run on the first while loop as we already added 1 to term_sum
        for i in range(1,n+1) :

            #multiplies the new fraction with itself (the previous term)
            each_term = each_term*(top_counter/bot_counter)
            term_sum = term_sum + each_term

            #numerator increases by 1 per iteration, while denominator by 2
            top_counter += 1
            bot_counter += 2

        calc_pi = 2*term_sum
        n += 1
        
    return calc_pi , n

#key function sort2, points to the second element in a list
#used for sorting the order of results(look below)
def sort2(list_pos):

    return list_pos[1]


#race function           
def race(precision,algorithms):

    #empty set y
    y =[]

    #runs through every algorithm in list
    for i in range(len(algorithms)):

            #gets the value and no of steps by calling each algorithm
            val, step = algorithms[i](precision)

            #adds the algorithm name and order to the list y in tuples
            y.append((i+1, step))

    #use the key function sort2 (refer function) to sort the algorithm based on the 
    y.sort(key = sort2)
    
    return y

#print_result function
def print_results(race_outcome):

    for i in race_outcome :
        print('Algorithm ' + str(i[0]) + ' finished in ' + str(i[1]) + ' steps')

    return None


res = race(0.01,[taylor, wallis, basel, spigot])
print_results(res)
    
