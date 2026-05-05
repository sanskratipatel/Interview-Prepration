arr =[2,14,12,1,11] 
n = len(arr) 
st = [] 
ans = [-1] * n 
new_arr = arr + arr
for i in range(len(new_arr) -1 , -1 , -1) :  
    while len(st ) > 0 and st[-1] <= new_arr[i] : 
        st.pop() 
    
    if i<n : 
        if len(st) > 0 and st[-1] > new_arr[i] : 
            ans[i] = st[-1] 
    st.append(new_arr[i])

print(ans)