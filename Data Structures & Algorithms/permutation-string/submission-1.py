class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def ispermutation(s1,s2) :
            c1 = [0]*26
            c2 = [0]*26
            for i in range(len(s1)):
                c1[ord(s1[i])-ord("a")]+=1  
                c2[ord(s2[i])-ord("a")]+=1
            return c1==c2
        if len(s1)>len(s2) :
            return False
        
        for r in range(len(s1),len(s2)+1):
            print(s2[r-len(s1):len(s1)])
            if ispermutation(s2[r-len(s1):r],s1) :
                return True
        return False        