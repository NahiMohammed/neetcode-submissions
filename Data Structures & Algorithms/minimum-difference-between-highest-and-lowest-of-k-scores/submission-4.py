class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res=nums[-1]-nums[0]
        L=0
        for R in range(k-1,len(nums)):
            res=min(res,nums[R]-nums[R-k+1])
        return res
        