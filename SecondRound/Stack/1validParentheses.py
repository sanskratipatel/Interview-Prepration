str1 = "{{()}}" 
st = []
for i in range(0 , len(str1)) : 
    if str1[i] in "{[(": 
        st.append(str1[i]) 
    else :
        if len(st) > 0 :
            e = st[-1]  
            if (e == "{" and str1[i] != "}" ) or (e == "[" and str1[i] != "]") or ( e == "(" and str1[i] != ")") :  
                 print("No") 
                 break  
            else : 
                st.pop() 
        else :
            print("No")  
            break 
if len(st) > 0  : 
    print("No")
else: 
    print("Yess")
                


