def cricular(arr) : 
    stack = [] 
    ans = [-1] * len(arr) 
    n = len(arr) 

    for i in range(n*2 -1 , -1, -1) : 
        while len(stack) >0 and stack[-1] <= arr[i%n] : 
            stack.pop() 
        if i <n : 
            if len(stack) != 0 : 
                ans[i] = stack[-1] 
            stack.append(i%n) 
        return ans