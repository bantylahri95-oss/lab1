lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

merged = list(set(lst1 + lst2))
print(*merged)