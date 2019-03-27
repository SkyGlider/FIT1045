#ANDREW PANG
#29/3/2019
#TASK 1b


def palin_check(word):
    rev = word[::-1]

    if rev == word :
        return True
    else:
        return False


z = open('palindromic.txt','r')
z = z.read()
z = z.replace(' ','')
z = z.split('\n')


for i in z :

    if palin_check(i) == True :
        print( i + ' is a palindrome')
        
    else:
        print( i + ' is not a palindrome')
            

