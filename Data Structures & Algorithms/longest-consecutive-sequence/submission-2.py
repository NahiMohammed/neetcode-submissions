class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        curr_streak=0
        res=0
        print(nums)
        for i in range(1,len(nums)) :
            if abs(nums[i] -nums[i-1])>1:
                res=max(res,curr_streak)
            else :
                if nums[i]==nums[i-1]+1:
                    curr_streak+=1
                    
        return max(res,curr_streak)

        