# Remove All Occurrence of a Character in a String
# Given a string and a character, remove all occurrences of the given character in the string. 
# Remove Leftmost Occurrence of a Character in a String
# Given a string and a character, remove the leftmost occurrence of the given character in the
s = "daabcbaabcbc" 

str1 = "abc" 

index = s.find(str1) 
print(s) 
if index != -1 : 
   s= s[:index] + s[index+ len(str1):] 
print(s)