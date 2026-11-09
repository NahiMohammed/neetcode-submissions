class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        l = 0 
        res= len(blocks)
        curr = 0
        for r in range(len(blocks)) : 
            print(f"l == {l} and r == {r} and curr = {curr}")

            if r-l+1>k :
                if blocks[l] =="W" :
                    curr-=1       
                l+=1

            if blocks[r] == "W" :
                curr+= 1
            if r-l+1==k :
                res=min(res,curr)
        return res
            

            
        