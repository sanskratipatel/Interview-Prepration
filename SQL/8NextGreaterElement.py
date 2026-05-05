def next_greater_brute_force(arr) : 
    ams = [-1] *len(arr) 
    for i in range(0 , len(arr)):
        for j in range(i+1 , len(arr)) :  
            if arr[j] > arr[i]  :
                ams.append(arr[j]) 
                break 
    return ams

def new_greater_element(arr) :  
    ans = [-1] * len(arr) 
    s1 = []
    for i in range(len(arr) -1,-1,-1) : 

        while len(s1) >0 and s1[-1]  <= arr[i]:
            s1.pop() 
        if len(s1) !=0 : 
            ans[i] =s1[-1]  
        s1.append(arr[i])   # missing

    return ans             # missing            
      
