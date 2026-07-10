class Solution:
    def maxDepth(self, s: str) -> int:
        o=0
        res=0
        for c in s :
            if c=='(':
                o+=1
                res=max(res,o)
            elif c==')':
                o-=1
        return res

        