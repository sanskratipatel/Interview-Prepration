arr= [4,5,3,7 ,8,2,4,9]

i = 0 
j = len(arr)-1 

max_container= -1 
w =0 
h =0


while i<=j:
    w = j- i
    h = min (arr[j] , arr[i]) 
    max_container = max(max_container , h * w) 

    if arr[i] < arr[j] : 
        i = i +1 
    else : 
        j = j-1 

print(max_container)