class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = [0]*26
        c2 = [0]*26

        n = len(s1)
        m = len(s2)

        if n>m:
            return False 
        
        for i in range(n) :
            c1[ord(s1[i])-ord("a")]+=1
            c2[ord(s2[i])-ord("a")]+=1
        if c1==c2 :
            return True
        
        for i in range(n,m):

            c2[ord(s2[i-n])-ord("a")]-=1


            c2[ord(s2[i])-ord("a")]+=1

            if c1==c2 :
                return True
        return False



        