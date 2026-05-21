arr = [7,1,5,3,6,4] 
mini_value = arr[0]
max_profit = 0
for i in range(0 , len(arr)) : 
    profit = arr[i] -mini_value
    max_profit  = max(max_profit , profit)
    if mini_value > arr[i] : 
        mini_value = arr[i] 
