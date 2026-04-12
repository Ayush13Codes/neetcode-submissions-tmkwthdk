class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # T: O(m * n * 4 ** L), S: O(L) where L = len of the word
        if not board or not board[0]:
            return False

        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            # Base case: If end of the word is reached, return true
            if i == len(word):
                return True

            # Check bounds, reusing the same char or different chars
            if (
                r < 0
                or c < 0
                or r >= ROWS
                or c >= COLS
                or (r, c) in path
                or board[r][c] != word[i]
            ):
                return False

            # Choose
            path.add((r, c))

            # Explore
            res = (
                dfs(r, c - 1, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r + 1, c, i + 1)
            )

            # Unchoose
            path.remove((r, c))

            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
