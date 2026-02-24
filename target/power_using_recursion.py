def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

base = int(input())
exp = int(input())
print(power(base, exp))