class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i=0
        n=len(t)
        j=0
        while j<len(s) and i<n :
            if s[j]==t[i] :
                i+=1
            j+=1
        return n-i
        