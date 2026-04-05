str1 = "abcde" 
goal  = "deabc" 

if len(str1) != len(goal) : 
    print("False")
else : 
    str2 = str1+ str1 
    if str2.find(goal) != -1 : 
        print("True")
    else : 
        print("False")