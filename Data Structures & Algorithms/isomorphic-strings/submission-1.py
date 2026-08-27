class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        done=set()
        new=s
        if len(s)!=len(t) :
            return False
        for i in range(len(s)) :
            if s[i] in done :
                continue
            else :

                new =new.replace(s[i],t[i])
                done.add(s[i])
                done.add(t[i])
        return new==t
                
             
        