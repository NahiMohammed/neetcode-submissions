class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:


        i=0
        res=[]
        locked=[False]*len(nums)
        def backtracking(sub) :
            if len(sub)==len(nums) :
                res.append(sub.copy())
            for j in range(0,len(nums)) :
                if j and nums[j]==nums[j-1] and not locked[j] and not locked[j-1]:
                    continue
                else :
                    if not locked[j]:

                        sub.append(nums[j])
                        locked[j]=True

                        backtracking(sub)

                        sub.pop()
                        locked[j]=False


        backtracking([])
        return res

        