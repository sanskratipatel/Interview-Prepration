str1 = "anagram" 
str2 = "mar" 

s = sorted(str1)
t = sorted(str2)

if t == s[:len(t)] : 
    print("Yayyy") 
else : 
    print("No")