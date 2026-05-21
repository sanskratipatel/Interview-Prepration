arr = [1,0,0,1,2,2,2,1,1,0] 

zeros = 0 
ones = 0 
twos = 0 

for i in range(0 , len(arr)) : 
    if arr[i] ==0 : 
        zeros = zeros +1 
    if arr[i] ==1 : 
        ones = ones +1 
    if arr[i] ==2 : 
        twos = twos +1 

for i in range(zeros) : 
    arr[i] = 0 

for j in range(zeros , (zeros+ ones)) : 
    arr[j] = 1 
for k in range((zeros + ones) , (zeros + ones+twos)): 
    arr[k] = 2