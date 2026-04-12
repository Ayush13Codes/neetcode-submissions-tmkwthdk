class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # T: O(n), S: O(n)
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False