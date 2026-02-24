def is_palindrome(s):
    return s == s[::-1]

s = input().strip()
print("Palindrome" if is_palindrome(s) else "Not Palindrome")