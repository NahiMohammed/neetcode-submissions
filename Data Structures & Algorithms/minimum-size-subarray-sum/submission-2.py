class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l=0
        
        if sum(nums) >=target :
            res = len(nums)
        else :
            return 0

        curr=0
        for r in range(l,len(nums)) :
            curr+=nums[r]
            if curr>=target :
                res=min(res,r-l+1)
                while curr>=target :
                    curr-=nums[l]
                    l+=1
                    if curr>=target :
                        res=min(res,r-l+1)
        return res


        