arr = [] 
ans = [-1] * len(arr) 

for i in range(0 , len(arr) ) :  
    for j in range(i +1 , len(arr))  : 
        if arr[j] > arr[i] :
            ans[i] = arr[j] 
            break 


ans = [-1]  * len(arr)  

st= []
for i in range( len(arr)-1 ,-1, -1)  :  
    if len(st) > 0 and st[-1] <= arr[i] : 
        while(len(st) > 0 and st[-1] <= arr[i]) : 
            st.pop() 
    if len(st) != 0 : 
        ans[i] = st[-1] 

    st.append(arr[i])
