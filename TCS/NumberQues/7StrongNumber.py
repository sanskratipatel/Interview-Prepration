def strong_number (num) : 
    ans = 0 
    original_num = num 
    while num != 0  : 
        digit = num %10  
        fact =1 
        for i in range(1 , digit +1) : 
            fact = fact * i 
        ans = ans +fact 
        num = num //10 
    if original_num == ans : 
        return True 
    else : 
        return False
