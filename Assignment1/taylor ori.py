#taylor function
import math
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

print(taylor(0.1))
