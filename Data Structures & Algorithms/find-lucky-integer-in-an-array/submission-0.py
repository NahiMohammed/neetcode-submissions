class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res=-1
        c=Counter(arr)
        for k , v in c.items() :
            if k==v:
                if k>res:
                    res=k

        return res
        