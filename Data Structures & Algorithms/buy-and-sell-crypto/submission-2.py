class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit=0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         diff=prices[j]-prices[i]
        #         profit=max(profit,diff)
        # return profit
        l=0
        r=1
        profit=0
        while r<len(prices):
            if prices[l]<prices[r]:
                a=prices[r]-prices[l]
                profit=max(profit,a)
            else:
                l=r
            r+=1
        return profit