class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # T: O(2 ** t/m), S: O(t/m) where m = min(candidates)
        res = []

        def dfs(i, cur, curSum):
            if curSum == target:
                res.append(cur[:])
                return

            if i == len(candidates) or curSum > target:
                return

            # Include cur candidate
            cur.append(candidates[i])
            dfs(i, cur, curSum + candidates[i])

            # Exclude cur candidate
            cur.pop()
            dfs(i + 1, cur, curSum)

        dfs(0, [], 0)
        return res
