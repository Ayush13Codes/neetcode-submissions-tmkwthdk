class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l, r = 0, 1

        while r < len(prices):
            # Profitable
            if prices[l] < prices[r]:
                p = prices[r] - prices[l]
                maxP = max(p, maxP)
            else:
                l = r
            r += 1
        return maxP

        # T: O(n), S: O(1)
            
