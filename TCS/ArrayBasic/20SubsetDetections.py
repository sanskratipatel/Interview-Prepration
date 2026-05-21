arr1 = [1,2,3,4,5]
arr2 = [3,4,5]

flag = True
 
for i in range(len(arr2)) : 
    if arr2[i] not in arr1: 
        flag = False  
        break  

s = ""
s1 = ""

for i in range(len(arr1)) :  
    s = s + str(arr1[i]) 
for j in range(len(arr2)) : 
    s1 =s1 + str(arr2[j])
print(s1 , s)
if s1 not in s : 
    print("Nooo")
