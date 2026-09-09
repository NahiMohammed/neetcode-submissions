class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        i=0
        res=[]
        locked=[False]*len(nums)
        def backtracking(sub) :
            if len(sub)==len(nums) :
                res.append(sub.copy())
            for j in range(0,len(nums)) :
                if not locked[j]:

                    sub.append(nums[j])
                    locked[j]=True

                    backtracking(sub)

                    sub.pop()
                    locked[j]=False


        backtracking([])
        return res
