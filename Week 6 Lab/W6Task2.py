#ANDREW PANG YONG CHEN
#FIT1045
#WEEK 6 LAB
#TASK 2

def greedy_coin_change(amount,denoms):
    
    #reverses to descending order
    denoms.sort(reverse = True)

    #initialize
    balance = amount
    num_need = len(denoms)*[0]

    #fills the num_need list with the LARGEST dnomination first
    for i in range(len(denoms)):
        
        while denoms[i] <= balance :
            num_need[i] += 1
            balance -= denoms[i]

    #reverses the num_need list to match the ascending order input list
    num_need.reverse()
    
    return num_need


print(greedy_coin_change(15,[1,7,13]))
