arr = [100 , 80, 60,70,60,75,85] 
ans = [0] * len(arr) 
st = [] 

for i in range(0 , len(arr)) : 
    while(len(st) > 0 and arr[st[-1]] <= arr[i]) : 
        st.pop() 
    if len(st) == 0 : 
       ans[i] = i+1 
    else : 
       ans[i] =  i-st[-1] 
    
    st.append(i) 
print(ans)