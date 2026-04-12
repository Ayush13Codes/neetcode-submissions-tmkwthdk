class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # T: O(n * m), S: O(n * m)
        res = defaultdict(list) # 100101 -> list of anagrams

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(word)
        
        return list(res.values())