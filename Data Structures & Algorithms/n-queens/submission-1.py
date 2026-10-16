class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        eliminated_colom = set()
        subset = []

        def backtracking(position, number):
            eliminated_colom.add(position)
            subset.append(position)
            if number == n - 1:
                print(subset)
                res.append(["." * c + "Q" + "." * (n - c - 1) for c in subset])
            else:
                for i in range(n):
                    if i not in eliminated_colom:
                        valid = True
                        for j in range(len(subset)):
                            row = j
                            col = subset[j]
                            if abs(row - (number + 1)) == abs(col - i):
                                valid = False
                                break
                        if valid:
                            backtracking(i, number + 1)

            subset.pop()
            eliminated_colom.remove(position)

        for i in range(n):
            backtracking(i, 0)

        return res
