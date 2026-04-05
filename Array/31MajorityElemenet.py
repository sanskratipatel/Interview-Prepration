arr = [1,2,3,4,2,3,3,3,3,3,3,3,3,5,2,3] 
my_dict = {}
for i in  range(0 , len(arr)) :
    if arr[i] not in my_dict : 
        my_dict[arr[i]] = 1 
    else:
        my_dict[arr[i]] = my_dict[arr[i]] + 1 

    
print(my_dict , len(arr))
for key in my_dict : 
    print(my_dict[key]) 
    if my_dict[key] > len(arr) //2:
        print("ANSWER is = " , key) 
        break



