class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dic = defaultdict(lambda: [-1, -1])
        for  i , c in enumerate(s) :
            if dic[c][0] == -1 :
                dic[c][0] = i 
            dic[c][1] = i 
        res = -1 
        for k , v  in dic.items() :
            if v[0]!=-1 and v[1]!=v[0] :
                res= max(res , v[1]-v[0]-1) 
        return res

        