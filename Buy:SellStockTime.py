class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        temp = 0
        l = 0
        r = l+ 1
        while r < len(prices):
            temp = max(prices[r] - prices[l],temp)
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                r += 1
            
        return temp