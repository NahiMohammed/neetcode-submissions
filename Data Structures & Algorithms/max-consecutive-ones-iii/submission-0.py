class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0 
        res= 0
        for r in range(len(nums)) : 
            if nums[r] == 0 :
                if k>0 :
                    k-=1
                else :
                    while nums[l]!=0 :
                        l+=1
                    l+=1


            res=max(res , r-l+1)
        return res