class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums[-1]=-1
        for j in range(len(nums)-2,-1,-1) :
            
            
            if j+nums[j]>len(nums)-1 :
                for k in range(j+1,len(nums)):
                    nums[k]=-1
            else :
                if nums[j+nums[j]]==-1 :
                    nums[j]=-1
        return nums[0]==-1


        