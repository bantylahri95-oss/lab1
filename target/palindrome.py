n = int(input().strip())
original = n
rev = 0
temp = abs(n)

while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10

if original == rev:
    print("Palindrome")
else:
    print("Not Palindrome")