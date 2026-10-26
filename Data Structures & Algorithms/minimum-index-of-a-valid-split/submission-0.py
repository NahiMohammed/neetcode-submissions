class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count = Counter(nums)
        dominant = max(count, key=count.get)
        pref = [0]*len(nums)
        for i in range(len(nums)) :
            pref[i] = (pref[i-1] if i > 0 else 0) + (nums[i] == dominant)
        
        total = count[dominant]

        for i in range(0 , len(nums)) :
            if pref[i]*2> i+1 and (total-pref[i])*2>(len(nums)-i-1) :
                return i
        return -1


        