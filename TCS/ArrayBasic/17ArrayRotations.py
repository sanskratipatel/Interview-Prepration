arr = [1,2,3,4,5]
k = 2 
n = len(arr) 
r = k%n
for i in range(0 , r+1) : 
    e = arr.pop()  
    arr.insert(0 ,e) 
print(arr)


for i in range(0 , r) : 
    e = arr.pop(0) 
    arr.append(e) 
print(arr)