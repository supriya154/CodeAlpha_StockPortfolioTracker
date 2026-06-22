stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420
}

total = 0

print("Available Stocks:")
for stock in stocks:
    print(stock, "-", stocks[stock])

n = int(input("How many stocks do you own? "))

for i in range(n):
    name = input("Enter stock name: ").upper()

    if name in stocks:
        qty = int(input("Enter quantity: "))
        total += stocks[name] * qty
    else:
        print("Stock not found!")

print("\nTotal Investment Value = $", total)

with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value = ${total}")

print("Data saved in portfolio.txt")