class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        triplets_set = set(map(tuple, triplets))
        allowed = [True]*len(triplets)
        for i  , t in enumerate(triplets) :
            if t[0]>target[0] or t[1]>target[1] or t[2]>target[2] :
                triplets_set.remove(tuple(t))
                allowed[i] = False
        res= [0 , 0  ,0 ]
        for i in range(len(allowed)) :
            if allowed[i] :
                for j in range(3) :
                    res[j]=max(res[j],triplets[i][j])
        return res == target


        