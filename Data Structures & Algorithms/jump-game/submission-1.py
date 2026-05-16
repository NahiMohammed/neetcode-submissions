class Solution:
    def canJump(self, nums: List[int]) -> bool:
        prev=-1
        i=0
        while i<len(nums)-1:
            print(f"prev= {prev}, i= {i}")
            prev=i       
            i=i+nums[i]
            if i==prev:
                return False

        if i==len(nums)-1 :
            return True
        else : 
            return False
        