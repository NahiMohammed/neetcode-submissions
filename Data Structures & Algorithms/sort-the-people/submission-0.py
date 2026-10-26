class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        pairs = sorted(zip(names, heights), key=lambda x: x[1] , reverse=True)
        result = [x[0] for x in pairs]
        return result
