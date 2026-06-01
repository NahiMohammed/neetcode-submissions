class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=0
        while True : 

            for i in range(0,len(strs)):
                if l>=len(strs[i]) or strs[i][l]!=strs[0][l]:
                    return  strs[0][0:l]
            l+=1

        