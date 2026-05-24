class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s=set()
        for i in range(len(nums)):
            s.add(nums[i])
        for i in range(len(nums)):
            if i not in s :
                return i 
        return 0
        

        