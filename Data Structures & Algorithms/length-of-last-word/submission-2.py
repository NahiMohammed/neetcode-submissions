class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res=0
        j=len(s)-1
        while s[j]==" ":
            j-=1
        while s[j]!=" ":
            j-=1
            res+=1
        return res
        