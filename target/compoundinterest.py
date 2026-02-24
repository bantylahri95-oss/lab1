p = float(input().strip())
r = float(input().strip())
t = float(input().strip())

ci = p * (1 + r/100) ** t - p
print(ci)