def fiboncci_series(n) : 
    if n ==1 : 
        return 1 
    if n==0 : 
        return 0
    return fiboncci_series(n-1) + fiboncci_series(n-2) 

print(fiboncci_series(10))