class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        ((()))
        (
        """
        res=[]
        seq=[]
        def backtracking(open,close) :
            if open==n and  close==n :
                res.append("".join(seq))
                return

            if open<n :
                seq.append("(")
                backtracking(open+1,close)
                seq.pop()
                
            if close<open :
                seq.append(")")
                backtracking(open,close+1)
                seq.pop()
        backtracking(0,0)
        return res

