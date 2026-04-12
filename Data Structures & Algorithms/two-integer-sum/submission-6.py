class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index

        for i, n in enumerate(nums):
            d = target - nums[i]
            if d in prevMap:
                return [prevMap[d], i]

            prevMap[n] = i

        # t:O(n), s:O(n)