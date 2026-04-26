def valid_parenthis (str1 ) : 
    stack1 = []  
    for i in range(0 , len(str1)) : 
        if str1[i] in "{[(":
            stack1.append(str1[i]) 

        else : 
            
            if len(stack1) == 0 : 
                return False 
            ch = stack1.pop() 

            if (str1[i] == ")"  and ch == '(') or (str1[i] == "]" and ch =='[')  or str1[i] == '}' and ch =='{' : 
                continue 
            else :
                return False  
    if len(stack1) !=0 : 
        return False 
    
    return True 
s1 = "{{(])}}" 
print(valid_parenthis(s1))
            

