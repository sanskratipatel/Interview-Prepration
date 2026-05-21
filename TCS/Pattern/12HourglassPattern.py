n= 5 
for i in range(n-1, -1 , -1) : 
    for j in range(n-i) : 
        print(" " ,end = " ") 
    for k in range(i) : 
        print("*" , end = " ") 
    for j in range(i+1) : 
        print("*" , end = " ") 
    print() 

for i in range(0 ,n) : 
    for j in range(n-i) : 
        print(" " ,end=" ") 
    for k in range(i) : 
        print("*" , end=" ") 
    for l in range(i+1) : 
        print("*" ,end = " ") 
    print()