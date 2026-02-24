d = eval(input())
for k, v in sorted(d.items(), key=lambda x: x[1]):
    print(k, v)