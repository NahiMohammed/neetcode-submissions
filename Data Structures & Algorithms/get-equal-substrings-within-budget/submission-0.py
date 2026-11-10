class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        diff = [0]* n
        for i in range(len(s)) :
            diff[i] = abs(ord(s[i])-ord(t[i]))
        res = 0
        l = 0 
        sum = 0
        for r in range(len(s)) :
            sum += diff[r]
            while sum>maxCost :
                sum-=diff[l]
                l+=1
            res=max(res , r-l+1)
        return res

