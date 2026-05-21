n=3

for i in range(1 , n+1) :  
    a = "A"
    for j in range(1 , n+1) : 
        print(a  , end=" ")  
        a =chr(ord(a) +1 )
    print() 
num = 1
for i in range(1 , n+1) : 
    for j in range(1 , n+1) :  
        print(num , end=" ") 
        num = num +1 
    print()

