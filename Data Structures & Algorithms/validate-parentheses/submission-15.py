class Solution:
    def isValid(self, s: str) -> bool:
        cto = {")":"(", "}":"{", "]":"["} # closing to opening brackets
        res = []

        for c in s:
            if c not in cto:
                res.append(c)
                continue
            
            if not res or res[-1] != cto[c]:
                return False

            res.pop()

        return not res

        # T: O(n), S: O(n)
