print("================================")
print("     STOCK PORTFOLIO TRACKER")
print("================================")

stocks = {
    "Apple": 180,
    "Tesla": 250,
    "Microsoft": 400,
    "Google": 150,
    "Amazon": 190
}

print("\nAvailable Stocks:")

for stock in stocks:
    print("-", stock)

stock_name = input("\nEnter stock name: ").title()

if stock_name in stocks:
    quantity = int(input("Enter quantity: "))

    price = stocks[stock_name]
    total = price * quantity

    print("\n----------------------------")
    print("Stock Name :", stock_name)
    print("Price      :", price)
    print("Quantity   :", quantity)
    print("Total Value:", total)
    print("----------------------------")

else:
    print("\nStock not found!")

print("\nThank you for using Stock Portfolio Tracker!")