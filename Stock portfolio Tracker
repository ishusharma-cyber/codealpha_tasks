stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140
}

portfolio = {}
total_investment = 0
total_current = 0

n = int(input("How many stocks do you want to add: "))

for i in range(n):
    name = input("Enter stock name: ").upper()
    qty = int(input("Enter quantity: "))
    buy_price = float(input("Enter buying price: "))

    if name in stock_prices:
        portfolio[name] = {"qty": qty, "buy": buy_price}
    else:
        print("Stock not available")

print("\n--- Portfolio ---")

for stock, data in portfolio.items():
    qty = data["qty"]
    buy_price = data["buy"]
    current_price = stock_prices[stock]

    investment = qty * buy_price
    current_value = qty * current_price

    total_investment += investment
    total_current += current_value

    print(f"{stock} -> Qty:{qty}, Buy:{buy_price}, Current:{current_price}")

print("\nTotal Investment:", total_investment)
print("Current Value:", total_current)
print("Profit/Loss:", total_current - total_investment)
