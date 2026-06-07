str1 = "{{[(])]}}"
st = []

valid = True

for i in range(len(str1)):

    if str1[i] in "{[(":
        st.append(str1[i])

    else:

        if len(st) == 0:
            valid = False
            break

        ch = st.pop()

        if (
            (ch == "{" and str1[i] != "}") or
            (ch == "[" and str1[i] != "]") or
            (ch == "(" and str1[i] != ")")
        ):
            valid = False
            break

if len(st) != 0:
    valid = False

print(valid)