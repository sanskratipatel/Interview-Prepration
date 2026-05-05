def longest_substring_without_repaeting_charcter(str1) : 
    maxi = 0 
    for i in range(0 , len(str1)) : 
        sete = set() 
        for j in range(i , len(str1)) : 
            if str1[j] in sete : 
                break  
            sete.add(str1[j])
            maxi = max(maxi , j-i+1) 
    print(maxi) 


def second_solutions(str1) : 
    i = 0 
    j = 0 
    my_dict = {} 
    maxi = 0
    while j < len(str1) : 
        if str1[j] in my_dict : 
            i = max(i , my_dict[str1[j]] +1)
         
        maxi = max(maxi, j-i+1) 
        my_dict[str1[j] ] = j 
        j = j+1  
    print(maxi) 

second_solutions("abcabcbb") 
longest_substring_without_repaeting_charcter("abcabcbb")