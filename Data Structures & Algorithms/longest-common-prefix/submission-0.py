class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=len(strs[0])-1
        for i in range(len(strs)-1):
            l=min(l,len(strs[i])-1,len(strs[i+1])-1)
            while strs[i][0:l+1]!=strs[i+1][0:l+1] and l>=0:
                l-=1
            if l==-1:
                return ""
        return strs[0][0:l+1]


        