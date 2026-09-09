class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        sub=[]
        def isPal(s) :
            return s==s[::-1]
        def backtracking(start) :
            if start ==len(s) :
                res.append(sub.copy())          
            for end in range(start+1,len(s)+1) :
                if isPal(s[start:end]) :
                    sub.append(s[start:end])
                    backtracking(end)
                    sub.pop()
        backtracking(0)
        return res
        