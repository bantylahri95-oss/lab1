s1 = input().replace(" ", "").lower()
s2 = input().replace(" ", "").lower()

print("Anagram" if sorted(s1) == sorted(s2) else "Not Anagram")