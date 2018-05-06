# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
# (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

# Update on 12/8/2017
# Solution 2:
    class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        a = prices[1:]
        b = prices[:-1]
        res = 0
        for i in range(len(a)):
            diff = a[i] - b[i]
            if diff > 0:
                res += diff
        return res
    
#Solution 1:    
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # only counting rising edge
        
        if len(prices) < 2:
            return 0
        else:
            total = 0
            for i in range(len(prices) - 1):
                profit = max(prices[i+1] - prices[i], 0)
                total += profit
            return total

or 
        profit = 0
        for i in range(1,len(prices)):
            profit += max(0, prices[i] - prices[i-1])
        return profit