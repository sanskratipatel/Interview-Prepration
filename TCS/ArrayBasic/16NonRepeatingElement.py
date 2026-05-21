arr = [1, 2, 3, 2, 1, 4, 5, 4] 
my_dict = {} 

for i in range(0 , len(arr)) : 
    if arr[i] not in my_dict : 
        my_dict[arr[i]] = 1 
    else : 
        my_dict[arr[i]] =  my_dict[arr[i]]+1 
for key in my_dict : 
    if my_dict[key] == 1 : 
        print("Non Repeating Elemenet = " ,key , my_dict[key] ) 
        break