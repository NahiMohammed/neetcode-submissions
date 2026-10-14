class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr_sum=0
        res=[]
        subset=[]
        def backtrack(i,curr_sum):

            if i>=len(nums) or curr_sum >=target :
                if curr_sum==target :
                    res.append(subset.copy())
                return 
            
            subset.append(nums[i])
            backtrack(i,curr_sum+nums[i])

            subset.pop()
            backtrack(i+1,curr_sum)

        backtrack(0,0)
        return res
        