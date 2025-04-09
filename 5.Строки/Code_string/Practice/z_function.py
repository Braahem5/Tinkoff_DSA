seach = "bac"
text = seach + "$" + "abacaba"
n = len(text)
Z = [0] * n
L = R = 0  # Window [L, R] that matches the prefix

# Start from 1, as Z[0] is always 0
for i in range(1, n):
    if i > R:  # Case 1: i is outside the current window
        L = R = i
        while (
            R < n and text[R] == text[R - L]
        ):  # Compare characters "condition 'R < n' so that it does not go out of bound"
            R += 1
        Z[i] = R - L  # Set Z[i] to the length of the match
        R -= 1  # Decrement R to the last matched index
    else:  # Case 2: i is inside the current window
        k = i - L  # Calculate the corresponding index in Z
        if Z[k] < R - i + 1:  # If the match is within the bounds
            Z[i] = Z[k]  # Copy the value
        else:  # If the match extends beyond the current window
            L = i  # Update L to the current index
            while R < n and text[R] == text[R - L]:  # Extend the match
                R += 1
            Z[i] = R - L  # Set Z[i] to the length of the match
            R -= 1  # Decrement R to the last matched index

y = len(seach)
ans = -1
for x in range(y, n):
    if Z[x] == y:
        ans = x


print(f"the sequnce is at {ans - y - 1} in the text")
print(Z)  # Output the Z-array
