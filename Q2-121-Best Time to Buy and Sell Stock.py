class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = 0
        max = inf
        profit = max - min
        for i in range(len(prices)):
            if prices[i]