class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # T: O(n), S: O(n)
        num_count = {} # num -> freq
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            num_count[n] = 1 + num_count.get(n, 0)

        for n, c in num_count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
