nums = [4,7,1,1,2,-3,-7,17,15,-18,-19] 
st = [] 

for i in range(0 , len(nums)) : 
    if nums[i] > 0 : 
        st.append(nums[i]) 
    else :
        while len(st) >0 and st[-1] > 0 and st[-1] < abs(nums[i]) :
            st.pop() 

        if len(st) >0 and st[-1] == abs(nums[i]) : 
            st.pop() 
        elif len(st) == 0 or st[-1] < 0 : 
             st.append(nums[i])    

print(st)