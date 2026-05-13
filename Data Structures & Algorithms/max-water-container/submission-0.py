class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # T: O(n), S: O(1)
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            bottleneck = min(heights[l], heights[r])
            water = (r - l) * bottleneck
            res = max(res, water)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res
