num = int(input().strip())
low = int(input().strip())
high = int(input().strip())

if low <= num <= high:
    print("In Range")
else:
    print("Out of Range")