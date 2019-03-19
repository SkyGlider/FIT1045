#ANDREW PANG YONG CHEN 30506271
#FIT1045
#16 MAR 2019
#ASSGNMENT 1 TASK 1 : PI
import math
def basel(precision) :
    
    calc_pi = 0
    n  = 0
    
    while abs( calc_pi - math.pi) > precision :
        
            n +=1
            
            term_sum = 0
            
            for i in range (1,n+1) :
                
                term_sum += 1/(i**2)


            calc_pi = math.sqrt(term_sum*6)
            
            


    return calc_pi , n


def taylor(precision) :
    
    runs_counter = 0
    calc_pi = 0
    
    while abs( calc_pi - math.pi ) > precision :
        
            runs_counter += 1
            term_sum = 0
            n = 0
            nums_counter = 1
            
            for i in range(1,runs_counter+1):

                    if i % 2 == 0 :
                        term_sum -= (1/nums_counter)
                    else :
                        term_sum += (1/nums_counter)
                    n+=1
                    
                    nums_counter += 2
                    
            
            
            calc_pi = 4*term_sum
            
            
    return calc_pi , n


def wallis(precision) :

   
    calc_pi = 0
    n = 0

    while abs( calc_pi - math.pi ) > precision :
        
        n += 1
        
        top_counter = 2
        bot_counter_1 = 1
        
        term_sum = 1
        
        for i in range(1,n+1) :

           
            

            term_sum = term_sum*((top_counter**2)/(bot_counter_1*(bot_counter_1+2)))

            top_counter += 2
            bot_counter_1 += 2

        calc_pi = 2*term_sum
        

    return calc_pi , n

def spigot(precision):

    calc_pi = 0
    n = 0

    while abs( calc_pi - math.pi ) > precision :
        
        top_counter = 1
        bot_counter = 3
        term_sum = 1
        each_term = 1
        
        for i in range(1,n+1) :
            
            each_term = each_term*(top_counter/bot_counter)
            term_sum = term_sum + each_term

            top_counter += 1
            bot_counter += 2

            

        calc_pi = 2*term_sum
        n += 1

        
    return calc_pi , n

def sort2(list_pos):

    return list_pos[1]
            
def race(precision,algorithms):
    
    y =[]
   
    for i in range(len(algorithms)):
            
            [ val, step ]  = algorithms[i](precision)
            
            y.append((i+1, step))


   
    y.sort(key = sort2)
    
    return y

def print_results(race_outcome):

    for i in range(len(race_outcome)) :
        y = race_outcome[i]
        
        print('Algorithm ' + str(y[0]) + ' finished in ' + str(y[1]) + ' steps')

    return None

usr_pre = float(input("Enter precision (eg. 0.01) :"))
res = race(usr_pre,usr_sel)
print_results(res)
    
