class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        i=0
        j=0
        res=0
        while i<len(g):
            while j<len(s) and s[j]<g[i]:
                j+=1
            if j==len(s):
                return res
            res+=1
            i+=1
        return res
        