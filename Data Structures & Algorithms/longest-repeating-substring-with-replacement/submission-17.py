class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        n=0
        res=0
        for r in range(1,len(s)) :
            if s[r]!=s[l] :
                if n<k :
                    res=max(res,r-l+1)
                    n+=1
                else :
                    while s[l]!=s[r] :
                        l+=1
                    for i in range(l+1 , r) :
                        n=0
                        if s[i]!=s[r] :
                            n+=1

            else :
                res=max(res,r-l+1)
        return res

            


        