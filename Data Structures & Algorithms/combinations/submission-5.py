class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        i=0
        res=[]
        def backtracking(i,sub) :
            if len(sub)==k :
                res.append(sub.copy())
            for j in range(i,n+1) :

                sub.append(j)

                backtracking(j+1,sub)
                sub.pop()

        backtracking(1,[])
        return res
