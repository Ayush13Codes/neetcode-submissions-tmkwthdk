class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      # T: O(n), S: O(n)
        prevMap = {} # num -> idx

        for i, n in enumerate(nums):
            d = target - n
            if d in prevMap:
                return [prevMap[d], i]
            prevMap[n] = i
        return -1
