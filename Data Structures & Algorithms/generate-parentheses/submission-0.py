class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtracking(open_p, close_p, s):
            if open_p == n and close_p == n:
                res.append(s)
                return

            if open_p < n:
                backtracking(open_p + 1, close_p, s + "(")

            if close_p < open_p:
                backtracking(open_p, close_p + 1, s + ")")

        backtracking(0, 0, "")
        return res