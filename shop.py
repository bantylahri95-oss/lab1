# shop billing system
notebooks = 3
price_notebook = 45
pens = 2
price_pen = 20
amount_given = 500

# Calculations
total_bill = (notebooks * price_notebook) + (pens * price_pen)
remaining_balance = amount_given - total_bill

# Output
print("Total Bill Amount: ₹", total_bill)
print("Remaining Balance: ₹", remaining_balance)
