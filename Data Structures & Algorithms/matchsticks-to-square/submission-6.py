class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s=sum(matchsticks)
        if s%4:
            return False
        else :
            a= s//4
        
        used=[False]*len(matchsticks)

        def backtracking(n,curr) :
            if n==4 :
                print("bingo")
                return True
            for i,match in enumerate(matchsticks) :
                if not used[i] :
                    if match+curr==a :
                        used[i]=True
                        if backtracking(n+1,0) :
                            return True
                        else :
                            return False
                    else :
                        if match+curr>a :
                            continue
                        else :
                            used[i]=True
                            if backtracking(n,curr+match) :
                                return True
                            used[i]=False

            return False




        return backtracking(0,0)
        