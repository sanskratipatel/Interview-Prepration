# . Number pyramid (1, 12, 123...) 

n = 5

num = "A"

for i in range(0, n) : 
    for j in range(n-i): 
        print(" ", end = " ") 
    for k in range(i+1) : 
        print(num , end = " ") 
    for l in range(i) :  
        print(num ,end = " " )   
    num = chr(ord(num)+1 )
    print()
num =  chr(ord(num)-2 )
for i in range(n-2 , -1 ,-1) :  
    for j in range(n-i) : 
        print(" ",end=" ") 
    for k in range(i+1) : 
        print(num , end = " ") 
    for l in range(i) : 
        print(num , end = " ") 
    num =  chr(ord(num)-1 )
    print()

for i in range(0 , n) :  
    num = "A" 
    for j in range(n-i) : 
        print(" ",end=" ") 
    for k in range(i+1) : 
        print(num , end = " ") 
        num =  chr(ord(num)+1 )
    for l in range(i) : 
        print(num , end = " ") 
        num =  chr(ord(num)+1 )
   
    print()