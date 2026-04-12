class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if self.isAlphaNum(c):
                newStr += c.lower() 

        return newStr == newStr[::-1]

    def isAlphaNum(self, c):
        return (ord('a') <= ord(c) <= ord('z') or 
                ord('A') <= ord(c) <= ord('Z') or
                ord('0') <= ord(c) <= ord('9'))

    #t: O(log n), s: O(log n)