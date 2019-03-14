from math import sqrt

def real_roots(a,b,c) :
    d = b**2 - 4*a*c
    
    if d < 0 :
        return("No real roots.")

    elif d == 0 :
        ans = (b*-1)/(2*a)
        return(ans)
    else :
        ans1 = ((b*-1)+(sqrt(d)))/(2*a)
        ans2 = ((b*-1)-(sqrt(d)))/(2*a)
        return(ans1,ans2)


a_in = float(input("Enter a value : "))
b_in = float(input("Enter b value : "))
c_in = float(input("Enter c value : "))

print("Roots :" + real_roots(a_in,b_in,c_in))



    
