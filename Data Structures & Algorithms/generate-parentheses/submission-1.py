class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        p = []

        def backtracking(open_count, close_count):
            print(p)
            if len(p) == 2 * n:
                res.append("".join(p))
                return
            if open_count < n:
                p.append("(")
                backtracking(open_count + 1, close_count)
                p.pop()
            if close_count < open_count:
                p.append(")")
                backtracking(open_count, close_count + 1)
                p.pop()

        backtracking(0, 0)
        return res