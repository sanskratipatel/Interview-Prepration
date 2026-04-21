arr = ["eat","tea","tan","ate","nat","bat"] 
my_dict = {}
for i in range(0 , len(arr)) : 
    temp = "".join(sorted(arr[i]))
    if temp in my_dict: 
        my_dict[temp].append(arr[i])
    else: 
         my_dict[temp] = [arr[i]] 
ans = [] 

for key in my_dict:
    ans.append(my_dict[key]) 

print(ans) 
# Time Complexity
# O(n * k log k) 

# Space Complexity
# O(n * k)