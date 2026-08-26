class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occ=[0]*26
        if len(s)!=len(t) :
            return False
        for i in range(len(s)):
            occ[ord(s[i])-ord('a')]+=1
            occ[ord(t[i])-ord('a')]-=1
        return occ==[0]*26
        