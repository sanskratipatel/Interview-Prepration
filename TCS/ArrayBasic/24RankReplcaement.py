arr = [40,10,20,30] 

temp = sorted(arr) 
my_dict = {}
for i in range(len(temp) ): 
    my_dict[temp[i]] = i +1 
print(my_dict) 

ans = [] 

for i in range(len(arr)) : 
    ans.append(my_dict[arr[i]]) 
print(ans)