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

i = 0  
j = len(height) -1 
ans = 0 
ans_water = 0
while(i<j) : 
    w = j-i 
    h = min(height[i] , height[j])  
    ans = w*h 
    ans_water = max(ans_water , ans) 

    if height[i]<height[j] : 
        i = i+1 
    else  : 
        j = j-1
    
print(ans_water)