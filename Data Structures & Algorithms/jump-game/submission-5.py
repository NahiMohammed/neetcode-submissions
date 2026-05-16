class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp=[False]*len(nums)
        dp[len(nums)-1]=True
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]<len(nums):
                dp[i]=(dp[i+nums[i]]==True)
            else :
                dp[i]=True
        print(dp)
        return dp[0]==True

        
#[0,0,0,1,0]