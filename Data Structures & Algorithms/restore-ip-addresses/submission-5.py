class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        1.0.1.023 
        1.0.10.23 x
        1.0.102.3 x 
        1.01.0.23 x 
        i<j<k
        """
        res=set()
        if len(s)>12:
            return []

        def valid(i,j):
            part=s[i:j]
            if int(part)>255 or len(part)>3 or (part[0]=="0" and part!="0") :
                return False
            else :
                return True

        def backtracking(i,j,k) :
            if k>=len(s):
                return 
            if valid(0,i) and valid(i,j) and valid(j,k) and valid(k,len(s)) :
                res.add(s[0:i]+"."+s[i:j]+"."+s[j:k]+"."+s[k:len(s)])
            
            backtracking(i,j,k+1)
            backtracking(i,j+1,k+1)
            backtracking(i+1,j+1,k+1)


        backtracking(1,2,3)
        return list(res)




        