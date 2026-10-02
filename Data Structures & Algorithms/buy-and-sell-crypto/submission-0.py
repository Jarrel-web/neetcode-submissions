class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_idx, sell_idx = 0 , 1
        maxP = 0
        while sell_idx < len(prices):
            if prices[buy_idx]<prices[sell_idx]:
                profit = prices[sell_idx] - prices[buy_idx]
                maxP = max(maxP,profit)
            else:
                buy_idx = sell_idx
            sell_idx +=1
        return maxP