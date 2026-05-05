def printnumber(n) : 
    if n ==1 : 
        print(n) 
        return 
    print(n) 
    printnumber(n-1) 
printnumber(10) 