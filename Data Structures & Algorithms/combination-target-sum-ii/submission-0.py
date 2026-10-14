class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        subset=[]
        nums.sort()
        def backtrack(i,curr_sum):


            if i>=len(nums) or curr_sum >= target :
                if curr_sum==target :
                    res.append(subset.copy())
                return 
            subset.append(nums[i])
            curr_sum+=nums[i]
            backtrack(i+1,curr_sum)
            subset.pop()
            curr_sum-=nums[i]
            while i+1<len(nums) and nums[i]==nums[i+1] :
                i+=1

            backtrack(i+1,curr_sum)

        backtrack(0,0)
        return res
        
        