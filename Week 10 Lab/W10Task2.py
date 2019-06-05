#ANDREW PANG YONG CHEN
#FIT1045
#WEEK 10 - TASK 2
#14 MAY 2019

def count(T,v):
    
    if v is None:
        return 0 
    else:
        left = count(T,T[v][0]) #recursive for left node
        right = count(T,T[v][1]) #recursive for right node
        return left + right + 1 # +1 adds current root (my own)

    
def balance(T,v):
    
    left = count(T,T[v][0]) #count left
    right = count(T,T[v][1]) #count right
    
    return left - right

tree = [(2,1),(3,None),(5,4),(None,None),(None,None),(None,None)]

print(count(tree,0))
