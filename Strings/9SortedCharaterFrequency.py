# Sort Characters By Frequency
t = "tree" 

my_dict = {} 
for i in range(0 , len(t)) : 
    if t[i] not in my_dict : 
        my_dict[t[i]] = 1 
    else : 
        my_dict[t[i]] = my_dict[t[i]] + 1 

my_dict = dict(sorted(my_dict.items(), key = lambda x:x[1], reverse = True))
print(my_dict)