class Solution:
    def maxScore(self, s: str) -> int:
        prefix = [0]*len(s)
        suffix = [0]*len(s)
        for i in range(0,len(s)):
            if s[i]=="0" :
                prefix[i]+=1
            if i :
                prefix[i]+=prefix[i-1]
        for i in range(len(s)-2,-1,-1):
            if s[i+1]=="1" :
                suffix[i]=1
            suffix[i]+=suffix[i+1]
        print(suffix)
        print(prefix)
        return max(suffix[i] + prefix[i] for i in range(len(s)))
                
            

        