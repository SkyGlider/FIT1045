usr_in = int(input('Enter a value : '))

for z in range (0,usr_in + 1) :
    if len(z) == 1 :
        print("00" + str(z))
    elif len(z) == 2 :
        print("0" + str(z))
    else :
        print(z)
        
