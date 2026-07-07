class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        k=0
        while i<len(nums):
            j=i
            while j+1<len(nums) and nums[j+1]==nums[i]:
                j+=1
            for _ in range(min(2,j-i+1)):
                nums[k]=nums[i]
                k+=1
            i=j+1
        return k
            
        