class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums)%2==1 :
            return False
        n=len(nums)
        return True