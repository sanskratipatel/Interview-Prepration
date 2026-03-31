arr = [1,2,3,6,4,5,7]
ans = 10 
real_ans = []
my_dict = {} 

for i in range(0 , len(arr)) : 
    remain= ans -arr[i] 
    if remain in my_dict :  
        real_ans = [remain, arr[i]]   
        break
    my_dict[arr[i]] = i 

print(real_ans)