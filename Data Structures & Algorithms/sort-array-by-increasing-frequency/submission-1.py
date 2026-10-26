class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        fr = [[]for _ in range(len(nums)+1)]
        res=[]
        for k , v in c.items() :
            fr[v].append(k)

        for i , ls in enumerate(fr) :
            if ls :
                for n in sorted(ls ,reverse=True) :
                    for _ in range(i) :
                        res.append(n)

        return res


        