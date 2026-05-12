def three_sum(arr) : 
   
    ans = set() 
    for i in range(0 , len(arr)) : 
        my_dict = {}
        for j in range(i+1 , len(arr)) :  
            remain = -(arr[i] + arr[j]) 
            if remain in my_dict :  
                res = [arr[i] ,arr[j] , remain]
                res.sort() 
                ans.add(tuple(res))
            my_dict[arr[j]] = 1 

    return ans

