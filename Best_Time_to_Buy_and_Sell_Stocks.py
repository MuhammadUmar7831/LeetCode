# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Optimal O(n) If the Profit get less than zero than update minimum and keep save the maximum Profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minimum = prices[0]
        for i in range(len(prices)):
            profit = max(prices[i] - minimum, profit)
            if prices[i] - minimum < 0:
                minimum = prices[i]
        return profit
        

# Brute Force (check Profit in every single case)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = 0
        profit = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if prices[j] - prices[i] > profit:
                    profit = prices[j] - prices[i]
        return profit
