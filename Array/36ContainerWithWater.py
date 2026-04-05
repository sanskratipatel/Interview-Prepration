height = [1,8,6,2,5,4,8,3,7] 
maxi_water = 0 
area = 0 

for i in range(0 , len(height)): 
    for j in range(i+1, len(height)):   
        w = j-i 
        h =min(height[j],height[i]) 
        area = h*w 
        maxi_water = max(maxi_water, area)

print(maxi_water)

# Two pointer approach 

