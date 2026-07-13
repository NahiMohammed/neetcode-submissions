class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        res=len(t)
        for i in range(len(s)):
            j=0
            if t[j]!=s[i]:
                continue
            else :                               
                j+=1
                for idx in range(i+1,len(s)):
                    if j<len(t) and s[idx]==t[j]:
                        j+=1
                res=min(res,len(t)-j)
        return res


        