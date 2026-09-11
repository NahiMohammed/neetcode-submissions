class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=sum(nums)
        for i in range(len(nums)) :
            cur=0
            for j in range(i,len(nums)):
                cur+=nums[j]
                if cur>res :
                    res=cur
        return res
        