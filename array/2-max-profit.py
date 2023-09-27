def maxProfit(prices):
    atual_profit = 0
    
    for i in range(1, len(prices)):
        first_value = prices[i-1]
        second_value = prices[i]
        
        if first_value < second_value:
            atual_profit = atual_profit + (second_value - first_value)

    return atual_profit


# Best Time to Buy and Sell Stock II
# Expected 7

prices = [7,1,5,3,6,4]

profit = maxProfit(prices)

print(profit)