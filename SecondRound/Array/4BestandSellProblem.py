def stock_buy_sell(arr) : 
    max_profit = 0 

    for i in range(0 , len(arr)) :  
        for j in range(i+1 , len(arr)) : 
            if arr[j] >arr[i] : 
                profit = arr[j]-arr[i] 
                max_profit = max(profit,max_profit) 

    return max_profit 


def stock_buy_sell(arr) : 
    max_profit = 0 
    min_price = arr[0] 

    for i in range(0 , len(arr)) : 
        if arr[i] < min_price : 
            min_price = min(arr[i] ,min_price) 
        profit = arr[i] - min_price
        max_profit = max(max_profit , profit)
    return max_profit

    