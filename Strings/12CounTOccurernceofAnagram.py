# Count Anagram Occurrence in a String 
# Given two strings s and p, return the number of occurrences of p's anagrams in s.

arr = "forxxorfxdofr"
p = "for" 

my_dict ={} 

for i in range(0 , len(p)) : 
    if p[i] not in my_dict : 
        my_dict[p[i]] = 1 
    else : 
        my_dict[p[i]] = my_dict[p[i]] + 1  
i = 0 
j = 0 
count = 0 

while (j<len(arr) ): 
   if (j-i+1) < len(p) : 
       j = j+1 
