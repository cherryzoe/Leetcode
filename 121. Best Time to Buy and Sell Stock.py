# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Example 1:
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5

# max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
# Example 2:
# Input: [7, 6, 4, 3, 1]
# Output: 0

# In this case, no transaction is done, i.e. max profit = 0.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # use two variable to store lowest price and best profit
        # the corner case is when input is [] or just one item
        
        if len(prices) < 2:
            return 0
        else:  
            lowest = prices[0]
            profit = 0
            for price in prices:
                lowest = min(lowest, price)
                profit = max(profit, price - lowest)
            return profit
            

Solution2: Kadane's algorithm
        
        if not prices:
            return 0
        
        maxProfit = curProfit = 0
        for i in range(1, len(prices)):
            curProfit = max(0, curProfit + prices[i] - prices[i-1])
            maxProfit = max(curProfit, maxProfit)
        return maxProfit