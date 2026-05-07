class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_price = prices[0]
        for i in range(1,len(prices)):
            if prices[i] > min_price:
                res = max(res,prices[i]-min_price)
            min_price = min(prices[i],min_price)
        # TC O(n) and SC O(1)
        return res