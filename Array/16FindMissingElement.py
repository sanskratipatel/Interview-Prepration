arr = [1,2,3,4,5,6,7,9] 

# Brute Force 
for i in range(0 ,len(arr) ) : 
    flag = 0
    for j in range(0 , len(arr)-1):
        if arr[j] == i : 
            flag = 1 
            break
    if flag == 0 : 
        print(i)
        break
sum = 0
total_sum = 0 
print(len(arr))
for i in range(0 , len(arr)+2) : 
    sum = sum + i  
    if len(arr)>i: 
        total_sum = arr[i] + total_sum

print(total_sum , sum) 
print(sum -total_sum)