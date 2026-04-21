str1 = "time to practice" 
# Minimum Window Substring 

j = 0 
s= "toc" 
my_dict ={}

for i in range(0 , len(s)) :
    if s[i] not in my_dict :
        my_dict[s[i]] = 1   
    else:
         my_dict[s[i]] =  my_dict[s[i]] +1 
count =len(my_dict)
i = 0 
mini = float('inf')
while(j<len(str1)) :
    if str1[j] in my_dict :
        my_dict[str1[j]] =  my_dict[str1[j]] -1 
        if  my_dict[str1[j]] ==0 :
            count =count -1 
    while count == 0 : 
        mini = min(mini , j-i+1)  
        if str1[i] in my_dict : 
            my_dict[str1[i]] = my_dict[str1[i] ] +1 
            if my_dict[str1[i]] > 0 :
              count = count +1
        i = i+1 
    j = j+1 
print(mini)
    