class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        profit = 0
        minimumStockValue = prices[0]
        
        for i in range(len(prices)):
            if minimumStockValue > prices[i]:
                minimumStockValue = prices[i]
            profit = max((prices[i]-minimumStockValue),profit)
        return profit
