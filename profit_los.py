#program to calculate profit or loss based on cost price and selling price
#input of cost price 
cp=float(input("Enter the cost price:"))
#to validate the cost price
if(cp<=0):
    print("Invalid cost price")
    exit()
    #exiting the program if cost price is invalid
else:#input of selling price
    sp=float(input("Enter the selling price:"))
    #to validate the selling price 
    if(sp<=0):
        print("Invalid selling pricce")
        exit()
        #exiting the program if sellling price is invalid
    else:
        #calculating profit or loss
        if(sp>cp):
        print("profit:",sp-cp)
        elseif(cp>sp):
        print("loss:",cpp-sp)
    else:
        print("No profit no  Loss")