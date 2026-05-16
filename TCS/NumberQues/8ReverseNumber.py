def reverse_number(num) : 
    num1 = num 
    rev = 0 

    while num1 != 0 : 
        rev = (rev*10 ) + (num1%10)  
        num1 = num1//10
    
     
    return rev 

print(reverse_number(101))