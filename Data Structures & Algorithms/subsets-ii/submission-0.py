class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset=[]
        res=[]
        nums.sort()
        def backtrack(nums,i) :
            if i>=len(nums):
                if i == len(nums): 
                    res.append(subset.copy())
                    return 
            subset.append(nums[i])
            backtrack(nums,i+1)
            subset.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1

            backtrack(nums,i+1)
        backtrack(nums,0)
        return res
            

        
        