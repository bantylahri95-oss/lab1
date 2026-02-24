def unique(lst):
    return list(set(lst))

lst = list(map(int, input().split()))
print(*unique(lst))