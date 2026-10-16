class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def isvalid(s) :
            if s[0]=="0" and s!="0" :
                return False
            if int(s)>255 or len(s)>3:
                return False

            return True
        res=[]
        sub=[]
        def backtracking(start) :
            if start == len(s) :
                if len(sub) ==4 :

                    res.append(".".join(sub))
                return 

            for end in range(start+1 , len(s)+1) :
                if isvalid(s[start:end]) :
                    sub.append(s[start:end])
                    backtracking(end)
                    sub.pop()
                
        backtracking(0)

        return res
        

        