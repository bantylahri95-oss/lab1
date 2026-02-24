n = int(input())
marks = {}

for _ in range(n):
    name, score = input().split()
    marks[name] = int(score)

topper = max(marks, key=marks.get)
print(topper)