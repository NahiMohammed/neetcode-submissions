class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr=[]
        def backtracking(open ,closed ) :
            if open == n and closed==n :
                res.append("".join(curr))
                return 
            if open<n :
                curr.append("(")
                backtracking(open+1,closed)
                curr.pop()
            if closed<open :
                curr.append(")")
                backtracking(open,closed+1)
                curr.pop()


        backtracking(0,0)
        return res

        