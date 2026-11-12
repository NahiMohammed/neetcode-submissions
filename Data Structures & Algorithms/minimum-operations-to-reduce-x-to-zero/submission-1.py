class Solution:
    def minOperations(self, nums: List[int], x: int) -> int: 
        s =sum(nums) 
        if x>s :
            return -1 
        limit = s-x 
        curr= 0 
        l=0
        best = -1
        n = len(nums)

        for r in range(len(nums)) : 
            curr += nums[r] 
            while curr>limit :
                curr-=nums[l]
                l+=1
            if curr == limit :

                best = max(best ,r-l+1)
        return len(nums) - best if best != -1 else -1 


