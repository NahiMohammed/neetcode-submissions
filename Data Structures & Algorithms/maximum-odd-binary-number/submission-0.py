class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c=0
        for  i in range(len(s)):
            if s[i]=='1':
                c+=1
        

        return (c-1)*"1"+(len(s)-c)*"0"+"1"

        