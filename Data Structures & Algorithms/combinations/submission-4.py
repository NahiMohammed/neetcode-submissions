class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        locked=[False]*(n+1)
        i=0
        res=[]


        def backtracking(i,sub) :

            if len(sub)==k :

                res.append(sub.copy())

            for j in range(i,n+1) :
                if not locked[j] :
                    sub.append(j)
                    locked[j]=True
                    backtracking(j+1,sub)
                    sub.pop()
                    locked[j]=False
        backtracking(1,[])
        return res
