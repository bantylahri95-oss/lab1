lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

common = set(lst1) & set(lst2)
print(*common)