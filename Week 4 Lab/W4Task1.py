#ANDREW PANG
#29/3/2019
#TASK 1


def palin_check(word):
    rev = word[::-1]

    if rev == usr_in :
        return True
    else:
        return False
    
usr_in = input("Enter a word : ")
print(palin_check(usr_in))
