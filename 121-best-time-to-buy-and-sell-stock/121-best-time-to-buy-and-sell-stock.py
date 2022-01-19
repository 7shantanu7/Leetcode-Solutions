class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices)==0):
            return 0
        low = prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i]<low:
                low = prices[i]
            
            if((prices[i]-low)>profit):
                profit =prices[i]-low
                
        return profit
            
           