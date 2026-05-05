height = [2,1,5,6,2,3] 
maxi = 0 
for i in range(0 , len(height)) : 
    min_h = height[i]
    for j in range(i , len(height)) :  
        min_h = min(min_h , height[j]) 
        area = min_h * (j-i+1) 
        maxi = max(maxi,area)
print(maxi)

