# Input values
amount = float(input("Enter transaction amount (₹): "))
account_age = float(input("Enter account age (in months): "))
is_international = input("Is the transaction international? (yes/no): ").lower()

# Condition check
if amount > 200000 and account_age < 6 and is_international == "yes":
    print("⚠️ Transaction flagged for manual verification.")
else:
    print("✅ Transaction is not flagged.")
