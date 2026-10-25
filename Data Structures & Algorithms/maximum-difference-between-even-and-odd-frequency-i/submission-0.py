class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)
        tab = [0]*101
        for k , v in c.items() :
            tab[v] =v
        right = len(tab)
        for i in range(len(tab)-2, -1,-2) :
            if tab[i]> 0 :
                right = i 
                break
        left = 0
        for i in range(0, len(tab),2) :
            if tab[i]> 0 :
                left = i 
                break
        return right-left