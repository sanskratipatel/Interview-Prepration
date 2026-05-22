roman = {
    1000 : "M",
    900 : "CM",
    500 : "D",
    400 : "CD",
    100 : "C",
    90 : "XC",
    50 : "L",
    40 : "XL",
    10 : "X",
    9 : "IX",
    5 : "V",
    4 : "IV",
    1 : "I"
} 

ans = "" 

num = 45 

for key in roman : 
     if num >= key : 
          count = num//key 
          ans = ans + roman[key] * count 
          num = num % key 
print(ans)