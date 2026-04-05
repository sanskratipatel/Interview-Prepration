# Permutation In String 
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s 

s1 = "ab"
s2 = "eidbaooo" 

my_dict = {}

for i in range(0 , len(s1)) :
    if s1[i] not in my_dict :  
        my_dict[s1[i]] = 1 
    else : 
        my_dict[s1[i]] = my_dict[s1[i]] + 1 


i = 0
j = 0 
while(j < len(s2)) : 
    if len(s1) < j-i+1 :  
        j = j +1 
        
