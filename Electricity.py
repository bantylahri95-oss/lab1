units = float(input("Enter electricity units consumed: "))
is_senior = input("Are you a senior citizen? (yes/no): ").lower()

bill = 0

if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    bill = (100 * 5) + (200 * 7) + ((units - 300) * 10)

# Apply 10% discount for senior citizen
if is_senior == "yes":
    bill *= 0.9

print("Total Electricity Bill: ₹", bill)
