class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        j=len(s)-1

        while j>=0 and s[j]==" " :
            j-=1
        res=0
        while j>=0 and s[j].isalpha() :
            res+=1
            j-=1
        return res

        