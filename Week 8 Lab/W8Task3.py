#ANDREW PANG
#FIT 1045
#WEEK 8 TASK 3
#12/4/2019

#Task 3a
def simple_recursive_binary_search(a_list,target):

    #exit condition for list
    #when list has 1 item, check if that item is target orelse, return false
    if len(a_list) == 1:
        if a_list[0] != target:
            return False
        else:
            return True

    #find the midpoint of index
    #if midpoint is target then return True
    #if midpoint less or more than target,
    #run recursion for list after or before target
    mid = int(len(a_list)/2)
    if a_list[mid] > target:
        return simple_recursive_binary_search(a_list[:mid],target)
    elif a_list[mid] < target:
        return simple_recursive_binary_search(a_list[mid:],target)
    elif a_list[mid] == target:
        return True
print('Simple binary search for [1,3,4,6,8], search 3')
print(simple_recursive_binary_search([1,3,4,6,8],3))


#Task 3b
def adv_recursive_binary_search(a_list,target,lo,hi):

    #exit condition when hi - lo = 1, checks list index for hi and lo
    #if none of the items in index hi and lo, return none
    if hi - lo == 1:
        if a_list[hi] == target:
            return hi
        elif a_list[lo] == target:
            return lo
        else:
            return None
        
    #find the midpoint of index in terms of hi and lo
    #this time the list used in recursion doesnt change
    #if midpoint is target, return index of midpoint
    #if midpoint more than target, hi = midpoint
    #otherwise, lo = midpoint
    mid = int((hi + lo)/2)
    if a_list[mid] > target:
        hi = mid
        return adv_recursive_binary_search(a_list,target,lo,hi)
    elif a_list[mid] < target:
        lo = mid
        return adv_recursive_binary_search(a_list,target,lo,hi)
    elif a_list[mid] == target:
        return mid
    
print('Advanced binary search for [1,3,4,6,8], search 3')   
print(adv_recursive_binary_search([1,3,4,6,8],3,0,4))


    
