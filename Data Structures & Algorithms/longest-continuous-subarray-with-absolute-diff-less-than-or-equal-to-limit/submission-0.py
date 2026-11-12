class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res= 1
        for i in range(len(nums)) :
            mi= nums[i]
            ma= nums[i]
            for j in range(i+1,len(nums)) :
                mi = min(mi,nums[j])
                ma = max(ma,nums[j]) 

                if ma - mi <= limit :
                    res = max(res,j-i+1)
                else :
                    break
        return res 



            
        