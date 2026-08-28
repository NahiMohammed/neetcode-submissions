class Solution:
    def minOperations(self, s: str) -> int:
        w1=0
        w2=0
        for i in range(len(s)) :
            if i%2==0 :
                if s[i]=='0' :
                    w1+=1
            else :
                if s[i]=='1':
                    w1+=1
        
        for i in range(len(s)) :
            if i%2==0 :
                if s[i]=='1' :
                    w2+=1
            else :
                if s[i]=='0':
                    w2+=1
                
        return min(w1,w2)
              
        