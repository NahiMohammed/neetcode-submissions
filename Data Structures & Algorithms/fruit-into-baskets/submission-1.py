class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        dic = {}
        res = 0

        for r in range(len(fruits)):
            if fruits[r] in dic or len(dic) < 2:
                dic[fruits[r]] = r
            else:
                fruit = min(dic, key=dic.get)
                l = dic[fruit] + 1
                del dic[fruit]
                dic[fruits[r]] = r

            res = max(res, r - l + 1)

        return res