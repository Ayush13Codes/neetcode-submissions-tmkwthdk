class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[r] > prices[l]:# Profitable
                p = prices[r] - prices[l]
                maxP = max(maxP, p)
            else:
                l = r
            r += 1
        return maxP

    # t: O(log n), s: O(1)
