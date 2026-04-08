# Maximum Size of subArray of size K 

arr = [2, 1, 5, 1, 3, 2] 
k =3 
sum = 0 
i = 0 
j = 0 

maxi_mun = float("-inf") 

while(j<len(arr)) :  
    sum = sum +arr[j] 
    if (j-i+1)< k : 
        j = j+1 

    elif (j-i+1) == k : 
        maxi_mun = max(sum , maxi_mun) 
        sum = sum - arr[i] 
        j = j+1
        i = i+1 
print(maxi_mun)