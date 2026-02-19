# Input
cart_value = float(input("Enter cart value (₹): "))
membership = input("Enter membership (Silver/Gold/Platinum/None): ").lower()
festival = input("Is it festival season? (yes/no): ").lower()

discounts = []

# Cart value discount
if cart_value >= 5000:
    discounts.append(10)
elif cart_value >= 2000:
    discounts.append(5)

# Membership discount
if membership == "silver":
    discounts.append(5)
elif membership == "gold":
    discounts.append(10)
elif membership == "platinum":
    discounts.append(15)

# Festival discount
if festival == "yes":
    discounts.append(20)

# Determine highest discount
if discounts:
    max_discount = max(discounts)
else:
    max_discount = 0

# Final calculation
discount_amount = (max_discount / 100) * cart_value
final_amount = cart_value - discount_amount

# Output
print("Highest Discount Applied:", max_discount, "%")
print("Final Payable Amount: ₹", final_amount)
