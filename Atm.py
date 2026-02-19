account_balance = float(input("Enter account balance: "))
withdraw_amount = float(input("Enter withdrawal amount: "))
daily_withdrawn = float(input("Enter amount already withdrawn today: "))
atm_cash = float(input("Enter ATM available cash: "))

DAILY_LIMIT = 50000

if withdraw_amount > account_balance:
    print("Transaction Failed: Insufficient account balance.")

elif (daily_withdrawn + withdraw_amount) > DAILY_LIMIT:
    print("Transaction Failed: Daily withdrawal limit exceeded (₹50,000).")

elif withdraw_amount > atm_cash:
    print("Transaction Failed: ATM has insufficient cash.")

else:
    account_balance -= withdraw_amount
    atm_cash -= withdraw_amount
    print("Transaction Successful!")
    print("Remaining Account Balance: ₹", account_balance)
