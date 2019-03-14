import math
a = [ 1 ,2 ,3 ]


def findmax(usrlist) :
    largest = 0
    for z in range(0,len(usrlist)) :
        if usrlist[z] > largest :
            largest = usrlist[z]
    return largest

def findmin(usrlist) :
    smallest = math.inf
    for z in range(0,len(usrlist)) :
        if usrlist[z] < smallest :
            smallest = usrlist[z]
    return smallest

max_val = findmax(a)
min_val = findmin(a)
print(max_val)
print(min_val)
d = max_val - min_val

if d == 0 :
    print("The range is narrow")
elif d > 0 and d <= 100 :
    print("The range is normal")
else :
    print("THe range is large")
