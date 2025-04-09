n = input("input the val :")

stack = []
bracket_seq = True
for x in n:
    if x in "{([":
        stack.append(x)
    elif x in "})]":

        if not stack:
            bracket_seq = False
            break

        last_element = stack.pop()
        if last_element == "[" and x == "]":
            continue

        if last_element == "{" and x == "}":
            continue

        if last_element == "(" and x == ")":
            continue

        bracket_seq = False
        break

if bracket_seq and not stack:
    print("Yes")
else:
    print("No")
