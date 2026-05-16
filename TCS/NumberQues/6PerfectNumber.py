def perfect_number(num) :
    ans = 0 
    for i in range(1 , num) : 
        if num%i == 0 : 
            ans = ans +1 
    
    if ans == num : 
        return True 
    return False 
