class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rotate(nums) :
            tmp=nums[-1]
            for i in range(len(nums)-1,-1,-1) :
                nums[i] =nums[i-1]
            nums[0]=tmp
        for _ in range(k):
            rotate(nums)        