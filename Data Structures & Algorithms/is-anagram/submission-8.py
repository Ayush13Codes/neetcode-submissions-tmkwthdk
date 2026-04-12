class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # T: O(n), S: O(n)
        if len(s) != len(t):
            return False

        countS, countT = {}, {} # char -> count

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        return countS == countT