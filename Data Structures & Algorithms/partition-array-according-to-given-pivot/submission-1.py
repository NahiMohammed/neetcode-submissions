class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small, equal, big = [], [], []

        for x in nums:
            if x < pivot:
                small.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                big.append(x)

        return small + equal + big