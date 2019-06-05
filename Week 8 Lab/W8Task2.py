#ANDREW PANG
#FIT 1045
#WEEK 8 TASK 2
#12/4/2019

#TASK 2a

#simple power using recursion
def simple_recursive_power(x, n):
    
    #if n = 0, x^0 is 1 hence return 1
    if n == 0:
        return 1
    
    return x*simple_recursive_power(x,n-1)

#execute
#print(simple_recursive_power(2,4))


#Task 2b

#advanced power using recursion
def advanced_recursive_power(x, n):

    #should n = 0, means input n is even, hence multiply by 1
    if n == 0:
        return 1
    
    #should n = 1, means input n is odd, hence, multiply by x
    elif n == 1:
        return x
    
    #use x^2 so that it runs in n/2 recursive steps
    return x*x*advanced_recursive_power(x,n-2)

print(simple_recursive_power(2,6))

    
    
    
