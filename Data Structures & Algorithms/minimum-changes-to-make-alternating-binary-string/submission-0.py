class Solution:
    def minOperations(self, s: str) -> int:
        res1=0
        res2=0
        for i in range(len(s)):
            if i%2==0 and s[i]!="0":
                res1+=1
            if i%2==1 and s[i]!="1":
                res1+=1
            if i%2==0 and s[i]!="1":
                res2+=1
            if i%2==1 and s[i]!="0":
                res2+=1


        
        return min(res1,res2)

        