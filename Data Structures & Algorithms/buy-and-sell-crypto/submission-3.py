class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        profit = float('-inf')

        for sell in range(len(prices)):
            current_profit = prices[sell] - prices[buy]
            profit = max(current_profit, profit)
            while prices[sell] < prices[buy]:
                buy = buy + 1
        return profit