class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        map=defaultdict(int)
        for w in words :
            for c in w :
                map[c]+=1
        for k,v in map.items() :
            if v%len(words)!=0 :
                return False
        return True 
        
        