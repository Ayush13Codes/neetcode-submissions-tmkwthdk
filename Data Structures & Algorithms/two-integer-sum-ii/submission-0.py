class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # T: O(n), S: O(1)
        l, r = 0, len(numbers) - 1

        while l < r:
            cur_sum = numbers[l] + numbers[r]

            if cur_sum == target:
                return [1 + l, 1 + r]
            
            if cur_sum > target:
                r -= 1
            else:
                l += 1
        
        return -1