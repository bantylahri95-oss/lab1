lst = list(map(int, input().split()))
k = int(input())

k = k % len(lst)
rotated = lst[-k:] + lst[:-k]
print(*rotated)