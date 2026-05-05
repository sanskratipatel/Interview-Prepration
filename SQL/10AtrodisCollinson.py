def astroid_collion(arr) : 
    stack =[] 
    n = len(arr) 

    for i in range(0, len(arr)) : 
        if arr[i] >0 : 
            stack.append(arr[i]) 
        else : 
            while len(stack) >0 and stack[-1] > 0 and stack[-1] < abs(arr[i]): 
                stack.pop() 
            if len(stack) > 0 and stack[-1] == abs(arr[i]) : 
                stack.pop() 
            elif len(stack) ==0  or stack[-1] <0 : 
                stack.append(arr[i])


      