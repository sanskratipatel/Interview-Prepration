def arm_strong_number(num) : 
    count = 0 
    n = num
    num1 = num
    while num !=0  :
        num = num //10
        count = count +1 
    ans = 0 
    while num1 != 0 : 
        ans = ans + (num1 % 10) ** count  
        num1 = num1 //10 
    if n == ans : 
        return True 
    else : 
        return False
    return ans  

print(arm_strong_number(1053))