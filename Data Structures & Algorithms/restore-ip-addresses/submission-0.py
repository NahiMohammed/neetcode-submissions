class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def valid(part):
            # vide
            if not part:
                return False
            if len(part)>3 :
                return False
            # > 255
            if int(part) > 255:
                return False
            # leading zero
            if len(part) > 1 and part[0] == "0":
                return False
            return True
        ##########################
        if len(s)> 12 :
            return[]
        ##########################
        res=[]
        def b (i,j,k):
            if not(i<j and j<k and k<len(s)) :
                return 
            if valid(s[:i]) and valid(s[i:j]) and valid(s[j:k]) and valid(s[k:]):
                res.append(s[:i]+"."+s[i:j]+"."+s[j:k]+"."+s[k:])
            b(i,j,k+1)
            b(i,j+1,k)
            b(i+1,j,k)

            

        b(1,2,3)
        return list(set(res))
        