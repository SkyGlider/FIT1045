#ANDREW PANG
#29/3/2019
#TASK 1b

#palindromic check function
def palin_check(word):
    rev = word[::-1]

    if rev == word :
        return True
    else:
        return False

#open,read and import data from a file to z
z = open('palindromic.txt','r')
z = z.read()
z = z.split('\n')

#Row operations
print('Row :')

for i in z :
    word = i.replace(' ','')
    if palin_check(word) == True :
        print( word + ' is a palindrome')
        
    else:
        print( word + ' is not a palindrome')

#Column operations
print('Column :')

#znew is a list of lists
znew = []
for k in z:
    k = k.split(' ')
    znew.append(k)
    
#loops every row first then every column
for i in range(len(znew[0])):
    charlist = []
    for j in range(len(znew)):
        charlist.append(znew[j][i])
        
    new_word = ''.join(charlist)
    if palin_check(new_word) == True :
         print( new_word + ' is a palindrome')
    else:
        print( new_word + ' is not a palindrome')
    


    
    
    
    
            

