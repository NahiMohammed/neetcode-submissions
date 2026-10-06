class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        occ=Counter(text)
        o=Counter("balloon")
        res=1
        print(occ)
        print(o)
        while True :
            for k, v in o.items():
                if v*res>occ[k] :
                    return res-1
            res+=1
        return res
        