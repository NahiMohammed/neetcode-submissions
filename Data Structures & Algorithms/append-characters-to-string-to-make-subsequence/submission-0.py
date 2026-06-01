class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        res=len(t)
        for i in range(len(s)):
            if s[i]==t[0]:
                j=i+1
                r=1
                while(r<len(t) and j<len(s)):
                    if s[j]==t[r]:
                        j+=1
                        r+=1
                    else :
                        j+=1
                res=min(res,len(t)-r)

            else :
                continue
        return res

        