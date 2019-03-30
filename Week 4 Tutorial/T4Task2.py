list_in = [ 'so' , 'the', 'iacecai', 'abc', 'mooom']
long_word = ''
for i in list_in :
    if len(i) > len(long_word):
        long_word = i

def palin_check(word):
    
    b = word[::-1]
    
    if word == b :
        return True

    else :
         return False


def vowel_check(word):
    word = word.lower()
    word = list(word)
    vowels = ['a','e','i','o','u']
    no_v = 0
    for i in word :
        if i in vowels:
            no_v += 1

    no_c = len(word) - no_v

    if no_v > no_c :
        
        return True
    
    else:
        
        return False
print(long_word)
print(palin_check(long_word))
print(vowel_check(long_word))


            
        
    
    
    
