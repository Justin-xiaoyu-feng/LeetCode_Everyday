# 121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        gain,cur_min = 0, 0
        cur_min = prices[0]
        for i in range(1, len(prices)):
            if prices[i] - cur_min > gain:
                gain = prices[i] - cur_min
            if prices[i] < cur_min:
                cur_min = prices[i]
        return gain