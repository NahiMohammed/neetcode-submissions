class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i  = len(strs[0]) 
        longest= -2
        flag = True
        for j in range(i) :
            if flag :
                for k in range(1,len(strs)) :


                    if j>= len(strs[k]) or strs[k][j] !=strs[0][j] :
                        longest = j-1
                        flag=False
                        break
        if longest ==-2 :
            return strs[0]
        if longest == -1 :
            return ""
        return strs[0][0:longest+1]
                        
        