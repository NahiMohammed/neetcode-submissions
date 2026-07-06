class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a=[0]*26
        b=[0]*26
        for i in range(len(s)) :
            a[ord(s[i])-ord("a")]+=1
        for i in range(len(t)) :
            b[ord(t[i])-ord("a")]+=1
        for i in range(26): 
            if a[i]>b[i] :
                return False
        return True

        