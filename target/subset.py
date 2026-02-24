s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
print("Yes" if s1.issubset(s2) else "No")