class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        max_profit=0

        for i in range(0,len(prices)):
            min_price=min(prices[i],min_price)
            max_profit=max(max_profit,prices[i]-min_price)
            
        return max_profit