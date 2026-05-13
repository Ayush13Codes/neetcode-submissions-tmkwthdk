class Solution:
    def isValid(self, s: str) -> bool:
        # T: O(n), S: O(n)
        cto = {"}": "{", ")": "(", "]": "["}
        stack = []

        for c in s:
            if c not in cto:
                stack.append(c)
                continue
            
            if not stack or stack[-1] != cto[c]:
                return False
            stack.pop()
        
        return not stack