def print_func(n) : 
    if n <1 : 
        return 1 
    print_func(n-1) 
    print(n) 
print_func(10) 

def print_reverse(n) : 
    if n < 1 :
        return 1 
    print(n) 
    print_reverse(n-1) 

print_reverse(10)