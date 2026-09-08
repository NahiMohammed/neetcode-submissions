class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        n=0
        res=0
        for r in range(1,len(s)) :
            #print(f"position r {r} s[r] = {s[r]} , and l={l} and s[l] = {s[l]} and res= {res}")
            if s[r]!=s[l] :
                if n<k :
                    res=max(res,r-l+1)
                    n+=1
                else :
                    l+=1
                    if s[l]!=s[l-1]:
                        n-=1
            else :
                res=max(res,r-l+1)
        return res

            


        