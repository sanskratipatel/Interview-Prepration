height = [20,34,40,20]
def frogjumprecursion(index,height) : 
    if index == 0 :return 0 
    jump1 = frogjumprecursion(index-1,height) + abs(height[index] - height[index-1])  
    if index>1 :
         jump2 = frogjumprecursion(index-2,height) + abs(height[index] - height[index-2])
    else: 
         jump2 = float("inf") 
    return min(jump2 , jump1) 
