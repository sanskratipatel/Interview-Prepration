def gcd(a, b) :
    while b != 0 : 
        temp = b 
        b = a%b 
        a =temp 
    return a 
print(gcd(12,16)) 

def lcm(a,b) : 
    return (a*b) // gcd(a,b)
