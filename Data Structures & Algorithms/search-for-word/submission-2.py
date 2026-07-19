class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        n = len(board)
        m = len(board[0])

        def backtracking(i, j, idx):
            # Found the whole word
            if idx == len(word):
                return True

            # Out of bounds
            if i < 0 or i >= n or j < 0 or j >= m:
                return False

            # Wrong character
            if board[i][j] != word[idx]:
                return False

            # Mark as visited
            temp = board[i][j]
            board[i][j] = "#"

            found = (
                backtracking(i + 1, j, idx + 1) or
                backtracking(i - 1, j, idx + 1) or
                backtracking(i, j + 1, idx + 1) or
                backtracking(i, j - 1, idx + 1)
            )

            # Restore the cell
            board[i][j] = temp

            return found

        # Try every cell as the starting point
        for i in range(n):
            for j in range(m):
                if backtracking(i, j, 0):
                    return True

        return False