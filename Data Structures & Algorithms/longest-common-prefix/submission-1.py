class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=0
        while True : 

            a=strs[0][l]
            for i in range(1,len(strs)):
                if l>=len(strs[i]) or strs[i][l]!=a:
                    return  strs[0][0:l]
            l+=1

        