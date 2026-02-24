lst = list(map(int, input().split()))
freq = {}

for num in lst:
    freq[num] = freq.get(num, 0) + 1

for key in freq:
    print(key, freq[key])