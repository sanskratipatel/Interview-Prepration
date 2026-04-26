s1 = "cadbzabcd"

max_length = 0

for i in range(len(s1)):
    my_dict = {}
    
    for j in range(i, len(s1)):   # start from i
        if s1[j] not in my_dict:
            my_dict[s1[j]] = 1
            len1 = j - i + 1
            max_length = max(max_length, len1)
        else:
            break

print(max_length)

print(max_length)