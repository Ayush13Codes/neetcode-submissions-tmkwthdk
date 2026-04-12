class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            # Profitable
            if prices[l] < prices[r]:
                p = prices[r] - prices[l]
                maxP = max(maxP, p)
            else:
                l = r
            r += 1

        return maxP 
        # Time: O(n), Space: O(1)