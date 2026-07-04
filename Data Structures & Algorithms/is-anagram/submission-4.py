class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter=[0]*26
        n=len(s)
        m=len(t)
        if n!=m :
            return False
        for i in range(n):
            counter[ord(s[i])-ord("a")]+=1
            counter[ord(t[i])-ord("a")]-=1
        return counter==[0]*26


        