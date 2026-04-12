class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # Val -> Index

        for i, num in enumerate(nums):
            d = target - num
            if d in prevMap:
                return [prevMap[d], i]
            prevMap[num] = i
        return -1

        # T: O(n), S: O(n)