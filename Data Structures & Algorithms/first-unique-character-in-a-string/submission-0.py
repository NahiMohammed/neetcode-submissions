class Solution:
    def firstUniqChar(self, s: str) -> int:
        occ = defaultdict(int)
        for c in s :
            occ[c]+=1 
        for i,c in enumerate(s) :
            if occ[c]==1 :
                return i
        return -1
        