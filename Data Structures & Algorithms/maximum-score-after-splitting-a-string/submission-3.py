class Solution:
    def maxScore(self, s: str) -> int:
        res=0
        curr=0
        if s[0]=="0" :
            curr+=1
        for i in  range(1,len(s)):
            if s[i]=="1" :
                curr+=1
        res=max(res,curr)
        print(curr)
        for i in range(2,len(s)-1) :
            print(i)
            
            if s[i-1]=="1" :
                curr-=1
            else :

                curr+=1
            if s[i]=="0" :
                curr+=1
            print(curr)
            res=max(res,curr)
        return res


        