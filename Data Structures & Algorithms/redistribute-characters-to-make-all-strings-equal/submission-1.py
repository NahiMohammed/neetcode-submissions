class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        occ=[0]*26
        for w in words :
            for c in w :
                occ[ord(c)-ord('a')]+=1
            
        for  i in range(26) :
            if occ[i]%len(words)!=0 :
                return False
        return True
        