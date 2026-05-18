class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # T: O(log n), S: O(1)
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2 # use floor div

            if nums[m] == target:
                return m

            if nums[m] < target:
                l += 1
            else:
                r -= 1

        return -1