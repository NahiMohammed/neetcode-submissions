class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        res=len(t)
        j=0
        for i in range(len(s)):
            
            if j<len(t) and s[i]==t[j]:
                j+=1
        res=min(res,len(t)-j)
        return res


        