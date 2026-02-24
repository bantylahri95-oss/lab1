t = tuple(map(int, input().split()))
print("Unique" if len(t) == len(set(t)) else "Not Unique")