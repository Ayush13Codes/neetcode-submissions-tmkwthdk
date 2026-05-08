class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # T: O(n * m), S: O(n * m)
        res = {}  # charCount -> list of anagrams

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            key = tuple(count)
            if key not in res:
                res[key] = []
            res[key].append(s)

        return list(res.values())
