# Union and intersection for Sorted Array
arr1 = [1,1,2,3,4,4,5,6] 
arr2 = [2,3,4,4,5,6] 
# Brute Force
set1 = set() 

for i in range(0 , len(arr1)) :
    set1.add(arr1[i]) 

for i in range(0 , len(arr2)) :
    set1.add(arr2[1]) 

ans = sorted(set1) 
print(ans) 

# Optimal Approach

