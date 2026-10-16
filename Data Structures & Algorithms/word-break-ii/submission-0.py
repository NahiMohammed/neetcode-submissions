class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res=[]
        sub=[]
        def backtracking(start) :
            if start == len(s) :
                res.append(" ".join(sub))
            for end in range(start+1,len(s)+1) :
                if s[start:end] in wordDict :
                    sub.append(s[start:end])
                    backtracking(end)
                    sub.pop()
        backtracking(0)
        return res
