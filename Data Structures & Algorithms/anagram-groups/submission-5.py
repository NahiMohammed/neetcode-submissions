class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def ana(s) :
            return s[::-1]==s
        dic=defaultdict(list)
        for s in strs  : 
            occ=[0]*26
            for i in range(len(s)) :
                occ[ord(s[i])-ord('a')]+=1
            dic[tuple(occ)].append(s)
        return list(dic.values()) 

        