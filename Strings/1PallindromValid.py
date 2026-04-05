str1 = "Ac3?e3c&a" 
st = 0 
end = len(str1)-1 


def isAlphaNumeric(ch) : 
    if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z' or (ch >= '0' and ch <= '9')):
        return True 
    return False

while(st<end) : 
    if isAlphaNumeric(str1[st]) == False:
        st = st+1 
        continue
    elif isAlphaNumeric(str1[end]) == False: 
        end = end -1 
        continue
    else : 
        if str1[st].lower() != str1[end].lower() : 
            print("NOT A PALLINDROME") 
            break
        else:
            st = st+1 
            end = end -1 
else:
    print("PALLINDROME")
