"""
\"\"\"
Coin Change Problem

Problem Definition:
    The problem is to find out how many different ways there are to make a specific amount of money 
    (in this case, £2) using any combination of given coin denominations (1p, 2p, 5p, 10p, 20p, 50p, £1, and £2).

Methodology:
    This solution uses a dynamic programming approach. It involves building up a table (array) in a bottom-up manner. 
    Each entry in the table stores the number of ways to make a certain amount of money. The algorithm iteratively 
    considers each coin denomination and updates the table with the number of ways to make each amount by including 
    the current coin denomination. This ensures that all possible combinations are considered efficiently.
\"\"\"
"""


def count_ways(coins, total):
    # Initialize an array where each index represents an amount, and the value at each index is the number of ways to make that amount.
    ways = [0] * (total + 1)
    ways[0] = 1  # There is exactly one way to make an amount of 0 (using no coins).

    # Iterate over each coin denomination
    for coin in coins:
        # Update the ways array for each amount that can be made with the current coin
        for i in range(coin, total + 1):
            ways[i] += ways[i - coin]

    return ways[total]

# Coin denominations and the total amount to make
coins = [1, 2, 5, 10, 20, 50, 100, 200]
total = 200

# Output the number of ways to make the total amount using the given coins
print(count_ways(coins, total))
