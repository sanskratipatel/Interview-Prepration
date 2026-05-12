arr = [[1,2,3],[2,3,4] , [6,5,3]] 

row = len(arr) 
col = len(arr[0]) 
for i in range(0 , row) : 
    for j in range(0 , col) : 
        print(arr[i][j] , end = " ") 
    print() 


sum = 0 
product = 1 

r= len(arr) 
c = len(arr[0]) 

for i in range(0 ,r ) : 
    for j in range(0 , c) : 
        sum = sum +arr[i][j] 
        product = product * arr[i][j]  

print()

for i in range(0 ,r ) : 
    for j in range(0 , c) : 
        if i <= j : 
           print(arr[i][j] ,end =" " ) 
        else: 
           print("*" , end = " ")
         
    print()


print()
print()
for i in range(0 ,r ) : 
    for j in range(0 , c) : 
        if i == j : 
           print(arr[i][j] ,end =" " ) 
        else: 
           print("*" , end = " ")
         
    print() 

print()
print()
for i in range(0 ,r ) : 
    for j in range(0 , c) : 
        if i+j == c-1 : 
           print(arr[i][j] ,end =" " ) 
        else: 
           print("*" , end = " ")
         
    print() 