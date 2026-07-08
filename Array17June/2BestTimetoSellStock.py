prices = [7,2,1,5,6,4,8] 

max_profit = 0
min_price = float("inf")
proft = 0
for i in range(0 , len(prices)) : 
    if min_price > prices[i] :  
        min_price = prices[i] 
    proft = prices[i] - min_price 
    max_profit = max(proft , max_profit) 
print(max_profit)
