arr = [1,2,3,2,4,5,1] 
my_dict = {}

for i in range(0 , len(arr)) :  
    if arr[i] not in my_dict : 
        my_dict[arr[i]] = 1 
    else: 
        my_dict[arr[i]] = my_dict[arr[i]] +1 

ans = sorted(my_dict.items(), key =lambda x:(x[1] ,x[0]) ) 
print(ans)
arr = ["cat", "dog", "apple", "dog", "cat", "banana"]

my_dict = {}

for i in range(len(arr)):

    if arr[i] not in my_dict:
        my_dict[arr[i]] = 1
    else:
        my_dict[arr[i]] = my_dict[arr[i]] + 1


ans = sorted(my_dict.items(),key=lambda x: (x[1] ,x[0]))

print(ans)
print(ans)