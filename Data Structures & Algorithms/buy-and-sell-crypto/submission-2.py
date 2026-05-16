class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices)==0):
            return 0
        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            #check if element > price exist in set yes
            if(prices[i]>min_price):
                profit = prices[i]-min_price
                if(profit>max_profit):
                    max_profit = profit
            if(prices[i]<min_price):
                min_price = prices[i]
        return max_profit