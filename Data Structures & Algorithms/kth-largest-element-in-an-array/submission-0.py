class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums=[-x for x in nums]
        heapq.heapify(nums)
        print(nums)
        while k>1 and nums: 
            heapq.heappop(nums)
            k-=1
        return -nums[0]

        