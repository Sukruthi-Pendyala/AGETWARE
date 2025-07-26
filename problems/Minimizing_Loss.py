def minimize_loss(prices):
    # Map each price to its year (0-indexed)
    price_to_year = {price: year for year, price in enumerate(prices)}
    
    # Sort prices in descending order to compare higher buy prices to lower sell prices
    sorted_prices = sorted(prices, reverse=True)
    
    min_loss = float('inf')
    best_buy_year = best_sell_year = -1

    for i in range(len(sorted_prices)):
        for j in range(i + 1, len(sorted_prices)):
            buy_price = sorted_prices[i]
            sell_price = sorted_prices[j]
            
            # Ensure that buying happens before selling
            if price_to_year[buy_price] < price_to_year[sell_price]:
                loss = buy_price - sell_price
                if 0 < loss < min_loss:
                    min_loss = loss
                    best_buy_year = price_to_year[buy_price] + 1  # +1 to make year human-readable
                    best_sell_year = price_to_year[sell_price] + 1

    return best_buy_year, best_sell_year, min_loss

# --- Input from user ---
try:
    num_years = int(input("Enter the number of years: "))
    print("Enter the house prices for each year, separated by space:")
    prices_input = list(map(int, input().strip().split()))

    if len(prices_input) != num_years:
        print(f"Error: You entered {len(prices_input)} prices but specified {num_years} years.")
    else:
        buy_year, sell_year, loss = minimize_loss(prices_input)
        if buy_year == -1:
            print("No loss possible. You can’t sell at a loss in this case.")
        else:
            print(f"\nBuy in Year {buy_year}, Sell in Year {sell_year}, with a Minimum Loss of: {loss}")

except ValueError:
    print("Invalid input. Please enter integers only.")
