#ANDREW PANG
#ASSIGNMENT 2 TASK 2

numbers = list('1234567890.')
prelist = { "+":2,
            "-":1,
            "*":3,
            "/":4,
            "^":5,
            "0":0 }

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
    
    
    expr = expr.replace(' ','')
    expr = list(expr)

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

    if not temp == '':
        newexp.append(float(temp))
    
    return newexp
        
#print(tokenization(instr))

def has_precedence(op1, op2):
    if prelist[op1] > prelist[op2] :
        return True
    else:
        return False

#print(has_precedence("+","^"))

def simple_eval(tokens):
    
    total_oper = 0
    for i in tokens :
        if i in prelist:
            total_oper += 1
    
    while not total_oper == 0:
        
        lasttoken = '0'
        for j in range(len(tokens)):
            if tokens[j] in prelist:
                pcheck = has_precedence(tokens[j],lasttoken)
                if pcheck == True :
                    operindex = j
                    lasttoken = tokens[j]
                
                    
        newtokens = tokens[:]
       
        for k in range(len(tokens)):
            if tokens[k] in prelist:
                if k == operindex:
                    #DO OPERATION 
                    answer = calc(tokens[k],tokens[operindex-1],tokens[operindex+1])
                    newtokens[operindex] = answer
                    del newtokens[operindex+1]
                    del newtokens[operindex-1]
        
        tokens = newtokens[:]
        total_oper -= 1
        
    return tokens[0]

#print(simple_eval([2.0, "+", 3.0, "*", 4.0, "^", 2.0, "+", 1.0]))
                
def complex_eval(tokens):
    sendover = False
    neweval = []
    gocalc = []
    for i in range(len(tokens)):
        if tokens[i] == '(':
            sendover = True
        elif tokens[i] == ')':
            print(gocalc)
            sendover = False
            inside_value = simple_eval(gocalc)
            gocalc = []
            neweval.append(inside_value)
        elif sendover == True :
            gocalc.append(tokens[i])
        else:
            neweval.append(tokens[i])
        
    final_ans = simple_eval(neweval)

    return final_ans

#print(complex_eval(["(", 2, "-", 7, ")", "*", 4, "∧", "(", 2, "+", 1, ")"]))

def complex_eval_pro(tokens):
    opencounter = 0
    for i in tokens:
        if i == '(':
            opencounter += 1
        
        
    while not opencounter == 0:
        newtoken = tokens[:]
        
        span = [0,0]
        for i in range(len(tokens)):
            if tokens[i] == '(':
                span[0] = i
            elif tokens[i] == ')':
                span[1] = i
                break

        sendover = []
        for j in range(span[0]+1,span[1]):
            sendover.append(tokens[j])
        
        ans = simple_eval(sendover)
        newtoken[span[1]] = ans
        del newtoken[span[0]:span[1]]
        
        tokens = newtoken[:]
        opencounter -= 1

    tokens = simple_eval(tokens)
    
    return tokens

#print(complex_eval_pro(["(","(", 2, "-", 7, ")","*", 10, ")", "*", 4, "^", "(", 2, "+", 1, ")"]))   
                
def evaluation(string):
    tokens = tokenization(string)
    print(tokens)
    return complex_eval_pro(tokens)

#print(evaluation("(2-7) * 4^(2+1)"))

usr_in = input("Enter an expression:")
print(usr_in)
print(evaluation(usr_in))

           
                    
                    
                
                
                
                

        
                
                
        
    
    
