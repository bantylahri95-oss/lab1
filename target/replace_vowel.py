s = input()
result = ""

for ch in s:
    if ch.lower() in "aeiou":
        result += "*"
    else:
        result += ch

print(result)