# Buy and Sell Stock  

arr = [7,1,5,3,6,4]  

profit = 0  
max_profit = 0  
for i in range(0 , len(arr)): 
    for j in range(i+1, len(arr)):  
        if arr[j]>arr[i] : 
            profit = arr[j] - arr[i] 
            max_profit = max(profit , max_profit) 
print(max_profit) 

max_profit1 = 0 
min_price = arr[0] 

for i  in range(1  , len(arr)): 
    if arr[i] > min_price : 
        max_profit1 = max(max_profit1 , arr[i]-min_price) 
    min_price = min (min_price , arr[i]) 

print(max_profit1)