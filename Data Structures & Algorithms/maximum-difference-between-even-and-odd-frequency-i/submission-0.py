class Solution:
    def maxDifference(self, s: str) -> int:
        c=Counter(s)
        a1=0
        a2=len(s)
        for k, v in c.items() :
            if v%2==1 and v>a1 :
                a1=v
            if v%2==0 and v<a2 :
                a2=v
        return a1 -a2

        