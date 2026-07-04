class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for s in strs : 
            occ=[0]*26
            for i in range(len(s)):
                occ[ord(s[i])-ord("a")]+=1
            d[tuple(occ)].append(s)
        return list(d.values())
                
        
        