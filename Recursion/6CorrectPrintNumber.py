def printnumber(n , number) : 
    if n >number :  
        return 
    print(n)
    printnumber(n+1 ,number) 


printnumber(1 ,10)