class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l= 0 
        res = 0 
        counter = defaultdict(deque)


        for r in range(len(nums)) :
            counter[nums[r]].append(r)
            if len(counter[nums[r]])>k :
                most_left = counter[nums[r]][0]
                for i in range(l , most_left+1) :
                    counter[nums[i]].popleft()

                l = most_left+1

            res = max(res , r-l+1)
        return res


