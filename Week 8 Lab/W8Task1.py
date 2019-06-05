#ANDREW PANG
#FIT 1045
#WEEK 8 TASK 1
#12/4/2019

#Recursion Reverse
def recursive_reverse(a_list):
    #If the recursive list is empty, terminates the recursion
    if len(a_list) == 0:
        return []
    #use slicing method at the list's last element
    return [a_list[-1]] + recursive_reverse(a_list[:-1])

print(recursive_reverse([1,2,3]))
