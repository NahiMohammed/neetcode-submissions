class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = 0

        while True:
            if l >= len(strs[0]):
                return strs[0]
            for i in range(1, len(strs)):
                

                if l >= len(strs[i]) or strs[i][l] != strs[0][l]:
                    return strs[0][:l]


            l += 1