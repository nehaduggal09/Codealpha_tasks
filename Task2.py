# Predefined stock prices (dictionary)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "AMZN": 3300
}

# Dictionary to store user's stock holdings
portfolio = {}

# Take user input
while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not found. Please choose from:", list(stock_prices.keys()))
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("Please enter a valid number for quantity.")

#  For Calculating total investment
total_investment = 0
print("\nYour Portfolio:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_investment += value
    print(f"{stock}: {quantity} shares x ${price} = ${value}")

print(f"\nTotal Investment: ${total_investment}")

# Optional: Save to a text file
save = input("Do you want to save this to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity
            file.write(f"{stock}: {quantity} shares x ${price} = ${value}\n")
        file.write(f"\nTotal Investment: ${total_investment}\n")
    print("Portfolio saved to 'portfolio_summary.txt'")
