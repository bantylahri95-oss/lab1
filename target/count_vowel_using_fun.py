def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")

s = input()
print(count_vowels(s))