class Solution:
    def isPalindrome(self, s: str) -> bool:
        sNew = ""

        for c in s:
            if not c.isalnum():
                continue
            sNew += c.lower()
        
        return sNew == sNew[::-1]