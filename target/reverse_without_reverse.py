lst = list(map(int, input().split()))
rev = []

for i in range(len(lst) - 1, -1, -1):
    rev.append(lst[i])

print(*rev)