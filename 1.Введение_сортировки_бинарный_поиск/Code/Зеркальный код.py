def longest_lexicographically_smallest_palindrome(n, s):
    # Step 1: Count character frequencies manually
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Step 2: Separate characters into even and odd occurrences
    even_part = []
    odd_char = ""

    for char in sorted(char_count.keys()):  # Sorting ensures lexicographical order
        count = char_count[char]
        if count % 2 == 1:  # If the count is odd
            if (
                odd_char == "" or char < odd_char
            ):  # Choose lexicographically smallest odd
                odd_char = char
        even_part.append(char * (count // 2))  # Add half of the character's occurrences

    # Step 3: Construct the palindrome
    first_half = "".join(even_part)  # Concatenate the even parts
    palindrome = first_half + odd_char + first_half[::-1]

    return palindrome


# Reading input
n = int(input())
s = input().strip()

# Generating the palindrome
result = longest_lexicographically_smallest_palindrome(n, s)

# Output the result
print(result)
