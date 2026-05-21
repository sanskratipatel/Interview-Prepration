str1 = "HELLO"

k = 2

ans = "" 

for i in range(len(str1)) : 
    ch = ord(str1[i]) - ord('A')
    shift = (ch + k) % 26 
    ans = ans + chr(shift + ord('A')) 
print(ans)