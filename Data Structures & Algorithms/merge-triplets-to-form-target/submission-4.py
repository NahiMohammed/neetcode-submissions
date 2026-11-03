class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        res= [0 , 0  ,0 ]
        for i, t in enumerate(triplets):
            if t[0]<=target[0] and t[1]<=target[1] and t[2]<=target[2]  :
                for j in range(3) :
                    res[j]=max(res[j],triplets[i][j])
            if res == target :
                return True
        return res == target


        