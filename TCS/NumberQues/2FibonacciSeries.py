def fibonacci_number(num) :  
    if num ==0 :
        return 0 
    if num ==1 :
        return 1 
    a = 0
    b = 1 
    fib =0
    for i in range(2, num +1) : 
        fib = a+b 
        a = b 
        b = fib 
    return fib