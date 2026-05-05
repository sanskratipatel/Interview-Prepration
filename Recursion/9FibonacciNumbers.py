def finbonacci_numbers(num) : 
    if num ==0 or num ==1 : 
        return num 
    return finbonacci_numbers(num-1) +finbonacci_numbers(num-2) 

print(finbonacci_numbers(15))