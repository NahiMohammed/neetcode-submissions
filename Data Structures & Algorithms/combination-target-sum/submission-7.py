class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subset=[]
        curr_sum=0
        res=[]
        def backtracking(i,subset,curr_sum) :
            if i>=len(nums) :
                return
            elif curr_sum>target :
                return 
            elif curr_sum==target :
                res.append(subset.copy())
                return 

            subset.append(nums[i])
            curr_sum+=nums[i]
            backtracking(i,subset,curr_sum)
            subset.pop()
            curr_sum-=nums[i]
            backtracking(i+1,subset,curr_sum)
        backtracking(0,subset,curr_sum)
        return res

        