lst = list(map(int, input().split()))
unique = list(set(lst))
unique.sort()
print(unique[-2])