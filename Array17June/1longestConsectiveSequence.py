def longestConsecutive(arr):
        #code here 
        
        count = 0 
        max_count = 0 
        
        for i in range(0 , len(arr)) : 
            count = count +1
            while i+1 in arr : 
                count = count +1 
                max_count = max(count ,max_count)  
    
            count = 0
            
        return max_count    