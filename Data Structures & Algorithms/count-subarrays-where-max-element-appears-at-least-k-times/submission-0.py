class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        freq = 0 
        m = max(nums)
        l = 0 
        res =0 
        for r in range(len(nums)) :
            if nums[r]==m :
                freq+=1
            while  freq>=k : 
                res += len(nums) - r
                if nums[l] == m:
                    freq -= 1
                l += 1
        return res
                
            


