class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atmost(k) :
            l=0
            res= 0 
            odd = 0 
            for r in range(len(nums )) :
                if nums[r]%2 == 1 :
                    odd+=1
                while k<odd :
                    odd -= nums[l]%2
                    l+=1
                res+= r-l+1
            return res
        return atmost(k)-atmost(k-1)

