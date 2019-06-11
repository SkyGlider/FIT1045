#ANREW PANG YONG CHEN
#FIT1045
#WEEK 10 - TASK 1
#14 MAY 2019

def quicksort(mylist):
    
    #return own list if len list = 1
    if len(mylist) < 2:
        return mylist

    #gets list of values less/more than pivot
    less_pivot = []
    more_pivot = []
    
    for x in mylist[1:]:
        if x <= mylist[0]:
            less_pivot.append(x)
        else:
            more_pivot.append(x)

    #recursion sort for both list less than and more than pivot
    less_sorted = quicksort(less_pivot)
    more_sorted = quicksort(more_pivot)

    return less_sorted + [mylist[0]] + more_sorted

print(quicksort([4,3,113,8,6,9]))
    
