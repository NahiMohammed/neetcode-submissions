class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n=len(s)
        m=len(t)
        if n!=m:
            return False
        a=[0]*26
        for i in range(n):
            a[ord(s[i])-ord("a")]+=1
            a[ord(t[i])-ord("a")]-=1
        return a==[0]*26        