str1 = "abcdefgtri" 
const = 0 
vowel = 0 

for i in range(0 , len(str1))  : 
    if (str1[i]=='A' or  str1[i]=='I'  or  str1[i]=='E'  or str1[i]=='O' or str1[i]=='U' or
        str1[i]=='a'  or  str1[i]=='i'  or  str1[i]=='e' or str1[i]=='o' or str1[i]=='u') : 
        vowel = vowel +1 
    else : 
        const = const +1 

