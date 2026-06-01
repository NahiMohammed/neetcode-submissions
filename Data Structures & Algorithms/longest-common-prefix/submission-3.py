class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=0
        while True : 

            for i in range(1,len(strs)):
                if l>=len(strs[i]) or l>=len(strs[0]) or strs[i][l]!=strs[0][l]:
                    return  strs[0][0:l]
            l+=1

        