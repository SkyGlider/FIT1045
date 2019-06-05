#ANDREW PANG
#30506271
#FIT1045
#WEEK 9 TASK 1
#Declare a list for index comparison
bra_open = [ '(','{','[' ]
bra_closed = [ ')','}',']' ]

#Task 1a - Explanation
#1 - adds to stack if open bracket
#2 - if closed check if stack if empty, if yes, invalid
#3 - if valid, pops the last item in stack
#4 - a valid string should return an empty stack (stack = [])

def basic_matching(string):
    string = list(string)
    stack = []
    for i in string:

        if i in bra_open:
            stack.append(i)
        elif i in bra_closed:
            if stack == []:
                return False
            y = stack.pop()
    if stack == [] :
        return True
    else:
        return False
    
#Excecute Task 1a
#print(basic_matching('(())'))
#print(basic_matching(')(()'))
#print(basic_matching('(()'))


#Task 1b - Explanation
#1 - adds to stack if its an open bracket
#2 - if closed bracket, checks the previous stack
#3 - pops the previous item in stack and compare index
#4 - if the type fits, then it continues
#5 - if it doesnt then return False
#6 - a valid string should give stack = [] in the end
    
def matching(string):
    string = list(string)
    stack = []

    for i in string:
        
        if i in bra_open:
            stack.append(i)
            
        elif i in bra_closed:
            
            if stack == [] :
                return False

            y = stack.pop()
            if bra_open.index(y) != bra_closed.index(i):
                return False
                
    if stack == []:
        return True
    else:
        return False

#Execute
print(matching(')[()]'))
print(matching('[(])'))
print(matching('[[(())]]'))
            
