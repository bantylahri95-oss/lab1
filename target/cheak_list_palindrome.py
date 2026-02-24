lst = list(map(int, input().split()))
print("Palindrome" if lst == lst[::-1] else "Not Palindrome")