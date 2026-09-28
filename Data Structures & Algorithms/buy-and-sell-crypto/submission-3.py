class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # lowest = prices[0]
        # profit = 0

        # for p in prices:
        #     lowest = min(lowest,p)
        #     profit = max(profit, p- lowest )

        # return profit

        l, r = 0,1
        maxProfit = 0

        while r<len(prices):
            if prices[l]< prices[r]:
                maxProfit = max(maxProfit, prices[r]-prices[l])
            else:
                l = r
            r+=1
        return maxProfit