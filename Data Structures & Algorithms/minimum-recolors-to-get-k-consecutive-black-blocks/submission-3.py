class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res=len(blocks)
        curr=0
        L=0
        for R,c in enumerate(blocks):
            if R-L==k-1:
                res=min(res,curr)

            if R-L>=k :
                
                if blocks[L]=="W":
                    curr-=1
                L+=1
            if blocks[R]=="W" :
                curr+=1
        return res
        