# Program to calculate Profit or Loss

cost_price = float(input("Enter the Cost Price: "))
selling_price = float(input("Enter the Selling Price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    profit_percent = (profit / cost_price) * 100
    print("Profit:", profit)
    print("Profit Percentage:", profit_percent, "%")

elif cost_price > selling_price:
    loss = cost_price - selling_price
    loss_percent = (loss / cost_price) * 100
    print("Loss:", loss)
    print("Loss Percentage:", loss_percent, "%")

else:
    print("No Profit, No Loss")