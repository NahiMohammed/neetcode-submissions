class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        occ=Counter(nums)
        for count in occ.values():
            if count % 2 != 0:
                return False
        return True
