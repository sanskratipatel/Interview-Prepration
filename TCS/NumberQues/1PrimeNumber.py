def prime_number(num) : 
    ans = []
    for i in range(2 , (num//2) +1) : 
        count = 0
        if num % i == 0 : 
            ans.append(i) 
    return ans
            
print(prime_number(10))