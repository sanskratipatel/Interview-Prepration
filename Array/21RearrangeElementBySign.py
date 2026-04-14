# # Rearrange Array By Sign 
# arr= [3,1,-2,-5,1,-4] 

# pos= [] 
# neg = [] 


# for i in range(0 , len(arr)) : 
#     if arr[i]<=0 : 
#         pos.append(arr[i]) 
#     else:
#         neg.append(arr[i]) 
# print(pos) 

# print(neg) 

# for i in range(0 , len(arr)//2) :
#     arr[2*i] = pos[i] 
#     arr[2*i+1] = neg[i] 

# print(arr)


# res= [0]* len(arr)  
# pos_index  = 0
# neg_index = 1
# for i in range(0 , len(arr)) :
#     if arr[i] <= 0 : 
#         res[pos_index] = arr[i] 
#         pos_index = pos_index +2
#     else: 
#         res[neg_index] = arr[i] 
#         neg_index = neg_index +2
# print(res) 
# Rearrange Array By Sign 
arr= [3,1,-2,-5,1,-4,-7,-71,-47]  
pos_arr = []
neg_arr = [] 

for i in range(0 , len(arr)) : 
    if arr[i] <= 0 : 
        neg_arr.append(arr[i]) 
    else : 
        pos_arr.append(arr[i]) 

n = len(pos_arr) 
m = len(neg_arr) 
i=0
res1 = []

while(i<n and i<m) : 
    res1.append(pos_arr[i])
    res1.append(neg_arr[i]) 
    i=i+1
   
if i<n :
    while(i<n) :  
        res1.append(pos_arr[i]) 
        i = i+1
if i<m :
    while(i<m) :  
        res1.append(neg_arr[i]) 
        i = i+1

        

print(res1)