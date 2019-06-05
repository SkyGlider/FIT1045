#ANDREW PANG YONG CEHN (30506271)
#FIT1045
#ASSIGNMENT 2 TASK 2 -Calculator
#STARTED: APRIL 2019
#COMPLETED: APRIL 2019
#SUBMITTTED: 13 MAY 2019

#initialize
numbers = list('1234567890.')
prelist = { "+":2,
            "-":1,
            "*":3,
            "/":4,
            "^":5,
            "0":0 }

#calc fucntion carries out operations
def calc(operation,a,b):
    
    if operation == "+" :
        return a+b
    elif operation == "-":
        return a-b
    elif operation == "*":
        return a*b
    elif operation == "/":
        return a/b
    elif operation == "^":
        return a**b
        

def tokenization(expr):
    
    #removes all spaces and lists the string
    expr = expr.replace(' ','')
    expr = list(expr)

    #creates a new expression by converting numbers from string to int
    newexp = []
    temp = ''
    for i in range(len(expr)):
    
        if expr[i] in numbers:
            temp = temp + str(expr[i])
        else:
            if not temp == '':
                newexp.append(float(temp))
            newexp.append(expr[i])
            temp = ''

    #incase the end of the string is a number
    if not temp == '':
        newexp.append(float(temp))
    
    return newexp

#debug: print(tokenization(instr))

def has_precedence(op1, op2):

    #compares the values op1, op2 in precedence list dictionary
    #returs tru if op1 has precedence over op2
    if prelist[op1] > prelist[op2] :
        return True
    else:
        return False

#debug: print(has_precedence("+","^"))

def simple_eval(tokens):

    #counts the number of operations
    total_oper = 0
    for i in tokens :
        if i in prelist:
            total_oper += 1

    #carries out until no more operations
    while not total_oper == 0:

        #checks and notes the highest precedence
        #notes the integers before and after the operation token
        lasttoken = '0'  #0 is just to kick start the list
        for j in range(len(tokens)):
            if tokens[j] in prelist:
                pcheck = has_precedence(tokens[j],lasttoken)
                if pcheck == True :
                    operindex = j
                    lasttoken = tokens[j]

        #ammends the tokens list, deletes the integers after and before the operation sign
        #changes the operation sign to the answer
        answer = calc(lasttoken,tokens[operindex-1],tokens[operindex+1])
        tokens[operindex] = answer
        del tokens[operindex+1]
        del tokens[operindex-1]
        total_oper -= 1
        
    return tokens[0]

#debug: print(simple_eval([2.0, "+", 3.0, "*", 4.0, "^", 2.0, "+", 1.0]))

def complex_eval_pro(tokens):
    
    #counts the total number of simple operations needed
    #1 bracket () = 1 simple operation, use number of open bracket to count
    opencounter = 0
    for i in tokens:
        if i == '(':
            opencounter += 1
        
    #runs until no more individual simple operations
    while not opencounter == 0:

        #finds and notes position of innermost open and close bracket 
        for i in range(len(tokens)):
            if tokens[i] == '(':
                bra_start = i
            elif tokens[i] == ')':
                bra_end = i
                break

        #generates new list, with all the tokens in the bracket
        sendover = []
        for j in range(bra_start+1,bra_end):
            sendover.append(tokens[j])

        #sends the list over for simple evaluation
        #sets the close bracket to answer
        #deletes all tokens from the opening bracket to token before close bracket
        ans = simple_eval(sendover)
        tokens[bra_end] = ans
        del tokens[bra_start:bra_end]
        
        opencounter -= 1

    #carries out simple eval for the now simplified list
    tokens = simple_eval(tokens)
    
    return tokens

#debug: print(complex_eval_pro(["(","(", 2, "-", 7, ")","*", 10, ")", "*", 4, "^", "(", 2, "+", 1, ")"]))   
                
def evaluation(string):
    tokens = tokenization(string)
    return complex_eval_pro(tokens)

#debug: print(evaluation("(2-7) * 4^(2+1)"))

#loop code for user input
while True:
    usr_in = input("Enter an expression:")
    
    if usr_in == "q" :
        break
    
    try:
        print(evaluation(usr_in))
    except:
        print('Exception: Invalid expression! Check brackets, negative integers or null division')
        continue
           
                    
                    
                
                
                
                

        
                
                
        
    
    
