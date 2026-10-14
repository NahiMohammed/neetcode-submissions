class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset=[]
        res=[]
        def backtrack(nums,i) :
            if i == len(nums): 
                res.append(subset.copy())
                return 
            subset.append(nums[i])
            backtrack(nums,i+1)
            subset.pop()
            backtrack(nums,i+1)
        backtrack(nums,0)
        return res
            

        