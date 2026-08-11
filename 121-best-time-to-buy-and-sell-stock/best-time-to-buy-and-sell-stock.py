class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #low and high concept
        #l=0
        #[1,4,2]

        l=prices[0] #1
        high=0
        profit = 0
        for i in range(1,len(prices)):
            high = prices[i]    #4
            temp = high - l
            if temp > profit:
                profit = temp
            if prices[i]<l:
                l = prices[i]
        return profit



        
            