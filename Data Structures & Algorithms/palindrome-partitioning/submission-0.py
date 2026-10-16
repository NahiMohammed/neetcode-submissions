class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        sub=[]
        def isPalyndrome(s) :
            return s==s[::-1]
        def backtracking(start) :
            if start ==len(s) :
                res.append(sub.copy())
                return 
            for end in range(start+1,len(s)+1) :
                if isPalyndrome(s[start:end]):

                    sub.append(s[start:end])
                    backtracking(end)
                    sub.pop()
        
        backtracking(0)


        return res


        