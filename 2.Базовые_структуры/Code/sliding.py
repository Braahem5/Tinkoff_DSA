# Given an array of integers and a number K, find the maximum sum of a subarray of size K.

# Example:
# Input: [2, 1, 5, 1, 3, 2], K = 3
# Output: 9 (The subarray with maximum sum is [5, 1, 3])
n = [2, 1, 5, 1, 3, 2]
K = 3

max_sum = sum(n[:3])  # n[0] + n[1] + n[2]
remove = 0

for y in range(K, len(n)):
    track = max_sum - n[remove] + n[y]
    max_sum = max(track, max_sum)
    remove += 1

print(max_sum)


# Given a string s and a string p, find all the start indices of p's anagrams in s. The order of output does not matter.

# Example:
# Input: s = "cbaebabacd", p = "abc"
# Output: [0, 6] (The substrings "cba" and "bac" are anagrams of "abc")

s, p = "cbaebabacd", "abc"
arr = []
left, right = 0, len(p)
window = s[left:right]
for x in range(len(s) - len(p)):
    if (p[0] in window) and (p[1] in window) and (p[2] in window):
        arr.append(x)
    left += 1
    right += 1

print(arr)
