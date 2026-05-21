n= 5 

for i in range(0 , n+1) : 
    num = n
    for j in range(i) : 
        print(num , end = " ") 
        num = num-1 
    print() 
print()
for i in range(1 , n+1) : 
    num = i 
    for j in range(i) : 
        print(num , end = " ") 
    num = num +1 
    print() 
num = n
for i in range(1 , n+1) : 
    for j in range(i) : 
        print(num , end =" ") 
    num = num-1 
    print() 

num = 0
for i in range(1 , n+1) : 
    for j in range(i) : 
        print(num , end =" ") 
    num = num+2 
    print() 
print()
for i in range(0 , n+1) : 
    for j in range(i) : 
        if  i%2 != 0 : 
            print("1" , end= " ") 
        else : 
            print("2" ,end= " ") 
    print()