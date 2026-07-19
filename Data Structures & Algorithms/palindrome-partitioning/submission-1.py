class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isP(s) :
            return s==s[::-1]
        
        path =[]
        res=[]
        def back(start) :
            if start==len(s):
                res.append(path[:])
                return 
            for end in range(start,len(s)):
                if isP(s[start:end+1]) :
                    path.append(s[start:end+1])
                    back(end+1)
                    path.pop()
        back(0)
        return res
        