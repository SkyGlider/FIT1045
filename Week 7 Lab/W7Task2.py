#ANDREW PANG
#FIT 1045
#WEEK 7 TASK 2
#12/4/2019

#Adapted from lecture slides, n is length of input list upperbounds
#last value is therefore, upperbounds
def bounded_lists(upperbounds):
    
    n = len(upperbounds)
    first = n*[0]
    last = upperbounds
    res = [first]
    while res[-1] != last:
        res += [lex_suc(res[-1],last)]
        
    return res

#lex_suc now takes another argument ub which is upperbounds         
def lex_suc(bitlst,ub):
    
    res = bitlst[:]
    i = len(res) - 1

    #if the value in current index is same as value in upperbounds, change to 0
    #then move one index backward
    while res[i] == ub[i]:
        
        res[i] = 0
        i -= 1

    #increment by 1 instead of going back to zero
    res[i] += 1
    
    return res

#execute
#print(bounded_lists([1,1,2]))

def brute_force_coin_exc(amount,denoms):
    
    #first instance when (number of coin * coin denom) => amount needed
    #is the upper bound for each denomination
    #generates a list of upper bounds for each denom
    n = len(denoms)
    each_max = n*[0]
    for i in range(n):
        total = 0
        while total < amount :
            total += denoms[i]
            each_max[i] += 1

    #get combinations of all denominations within the upperbounds of each denom
    all_combi = bounded_lists(each_max)
    leastnumofcoin = sum(each_max)
    
    #feasibility check for each combinations (number*coin value = amount needed)
    for i in all_combi :
        
        each_total = 0
        for j in range(n):
            each_total += i[j] * denoms[j]

        #notes the minimum number of coins needed
        if each_total == amount:
            if sum(i) < leastnumofcoin :
                leastnumofcoin = sum(i)
                best_combi = i

    return best_combi

#execute
total_needed = 8
denoms_available = [1,4,5]
print(brute_force_coin_exc(total_needed,denoms_available))
                


            
        

