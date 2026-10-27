class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res=[]
        res.append(s[0:spaces[0]])
        print(res)
        for i in range(1,len(spaces)) :
            res.append(s[spaces[i-1]:spaces[i]])
        res.append(s[spaces[-1]:])
        return " ".join(res)

