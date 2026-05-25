class Solution:
    def ispalindrom(self, s: str):
        l= 0
        r= len(s)-1
        while l<r :
            if s[l]!=s[r] :
                return False
            l+=1
            r-=1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtracking(start,acc) :
            if start==len(s) :
                res.append(acc.copy())
            for end in range(start,len(s)):
                sub=s[start:end+1]
                if self.ispalindrom(sub) :
                    acc.append(sub)
                    backtracking(end+1,acc)
                    acc.pop()


        backtracking(0,[])
        return res

    
        