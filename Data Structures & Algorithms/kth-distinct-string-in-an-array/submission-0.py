class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        res=[]
        occ=defaultdict(int)
        for c in arr :
            occ[c]+=1
        for key, v in occ.items() :
            if v==1 :
                res.append(key)
        if len(res)>=k:
            return res[k-1]
        return ""

        