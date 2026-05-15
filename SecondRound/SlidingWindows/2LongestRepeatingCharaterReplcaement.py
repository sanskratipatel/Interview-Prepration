def longest_repeating_character_replacement(arr , k) : 
    
    ans = 0 

    for i in range(0 , len(arr)) : 
        
        hashmap = {} 
        max_freq = 0 

        for j in range(i , len(arr)) : 
            
            if arr[j] not in hashmap : 
                hashmap[arr[j]] = 1 
            else : 
                hashmap[arr[j]] = hashmap[arr[j]] + 1 
            
            max_freq = max(max_freq , hashmap[arr[j]]) 

            changes = (j-i+1) - max_freq 

            if changes <= k : 
                ans = max(ans , j-i+1) 
    
    return ans


arr = "AABABBA"
k = 1 

print(longest_repeating_character_replacement(arr , k)) 

def longest_repeating_character_replacement_optimal(arr , k) : 
    i = 0 
    j = 0 
    my_dict = {} 
    ans = 0 
    max_freq = 0 
    while j< len(arr) : 
        if arr[j] not in my_dict : 
            my_dict[arr[j]] = 1 
        else : 
            my_dict[arr[j]] = my_dict[arr[j]] +1 
        max_freq = max(max_freq , my_dict[arr[j]]) 
        if (j-i+1) -max_freq > k : 
            my_dict[arr[i]] = my_dict[arr[i]] -1 
            i = i+1 
        ans = max(j-i+1 , ans) 
        j = j+1 
    return ans 

    
   


arr = "AABABBA"
k = 1 

print(longest_repeating_character_replacement(arr , k)) 

 
