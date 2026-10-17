class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res=0
        def isPrefixAndSuffix(s1 , s2 ) :
            if len(s2)<len(s1) :
                return False
            return s2[0:len(s1)] == s1 and s2[len(s2)-len(s1):len(s2)]==s1
        for i in range(len(words)) :
            for j in range(i+1,len(words)) :
                if isPrefixAndSuffix(words[i],words[j]) :
                    res+=1
        return res
            