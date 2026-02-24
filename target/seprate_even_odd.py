lst = list(map(int, input().split()))

even = [x for x in lst if x % 2 == 0]
odd = [x for x in lst if x % 2 != 0]

print("Even:", *even)
print("Odd:", *odd)