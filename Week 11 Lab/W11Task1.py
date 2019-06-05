#gets the max child's index
def max_child(v,heap):
    
    l = None
    r = None

    #checks if the child exists or not
    if not (2*v+1) > len(heap)-1:
        l = 2*v+1

    if not (2*v+2) > len(heap)-1:
        r = 2*v+2
    
    #if sterile, return None
    if l == None and r == None:
        return None

    #orelse return the child's index
    if r == None:
        return l
    elif l == None:
        return r
    elif heap[l] > heap[r]:
        return l
    else:
        return r
    

def insert(heap,item):

    #set current index to last item inlist
    index = len(heap)
    heap.append(item)

    #while the index is not the root, swaps parent with child when:
    #index value is greater than parent
    while index != 0:
        parent = (index -1 )//2
        if heap[index] > heap[parent]:
            heap[index], heap[parent] = heap[parent], heap[index]
        else:
            break #break once it is already sorted
        index = parent
 
    return heap

def extract_max(heap):

    #takes the uppermost item as the max value
    max_val = heap.pop(0)
    #take the bottom right value and put it on top
    nxtroot = heap.pop() 
    heap = [nxtroot] + heap
    
    #initialize me(0) and mychild
    me = 0
    mychild = max_child(me,heap)
    
    #while my child is not none, swaps me and mychid id mychild is bigger than me
    while  mychild != None:
        if heap[mychild]  > heap[me]:
            heap[mychild] ,heap[me] = heap[me],heap[mychild]
        else:
            break #break once sorted
        
        me = mychild
        mychild = max_child(me,heap)
    
    return max_val, heap

def heapsort(items):

    #put unsorted items into heap
    myheap = []
    for i in items:
        myheap = insert(myheap,i)

    sortedlist = []
    #loop that extracts max until heap has 1 item left 
    while len(myheap) != 1:
        val , myheap = extract_max(myheap)
        sortedlist.append(val)
        
    #add the last item in heap to sorted list
    return sortedlist + myheap
        
#Eggsarecute
print(heapsort([200,1,20,4,7,3]))


    
