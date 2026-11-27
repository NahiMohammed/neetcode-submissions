class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        occ = [0]*26
        for w in words : 
            for c in w  :
                occ[ord(c)-ord("a")]+=1
        n = len(words)
        for i in range(26) : 
            if occ[i]%n != 0 :
                return False 
        return True