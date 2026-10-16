class Solution:
    def totalNQueens(self, n: int) -> int:

        res = []
        eliminated_colom = set()
        subset = []

        def backtracking(row):
            if row == n:
                res.append(["." * c + "Q" + "." * (n - c - 1) for c in subset])
                return
            for i in range(n):
                if i in eliminated_colom:
                    continue
                valid = True
                for j in range(len(subset)):
                    if abs(j - row) == abs(subset[j] - i):
                        valid = False
                        break
                if valid:
                    eliminated_colom.add(i)
                    subset.append(i)
                    backtracking(row + 1)
                    subset.pop()
                    eliminated_colom.remove(i)

        backtracking(0)
        return len(res)
        