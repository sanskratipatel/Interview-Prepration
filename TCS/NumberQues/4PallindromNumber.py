def pallindrom_number(num) : 
    num1 = num 
    rev = 0 

    while num1 != 0 : 
        rev = (rev*10 ) + (num1%10)  
        num1 = num1//10
    
    if num == rev :
        return True 
    else : 
        return False 

print(pallindrom_number(101))