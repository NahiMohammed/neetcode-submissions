class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        res=len(t)
        for i in range(len(s)):
            j=0

            if t[j]!=s[i]:
                continue
            else :
                curr=1
                
                j+=1
                for idx in range(i+1):
                    if j<len(t) and s[idx]==t[j]:
                        j+=1
                        curr+=1
                res=min(res,len(t)-curr)
        return res


        