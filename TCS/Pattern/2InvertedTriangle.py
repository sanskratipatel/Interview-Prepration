n =5
for i in range(n,-1,-1) :
    for j in range(0 , i) : 
        print("*" , end = " ")
    print()  

for i in range(n, -1, -1) : 
    for j in range(n-i) : 
        print(" ",end = " ") 
    for k in range(i) : 
        print("*" ,end=" ")
    print()