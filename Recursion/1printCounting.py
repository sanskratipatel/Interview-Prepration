def number_print(num): 
    if num==1 :
        print(num ) 
        return 
    print(num) 
    number_print(num-1) 

number_print(10)