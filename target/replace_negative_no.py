lst = list(map(int, input().split()))
lst = [0 if x < 0 else x for x in lst]
print(*lst)