for i in range(0 , 4) : 
    for j in range(0 , i) : 
        print("*" , end=" ") 
    print() 

for i in range(0 , 4) : 
    for j in range(0 , i) : 
        print("*" , end=" ") 
    print() 

n = 5
for i in range(0 ,n) : 
    for j in range(n-i) : 
        print(" ", end=" ")
    
    for k in range(i ):  
        print("*" ,end = " ")
    print()