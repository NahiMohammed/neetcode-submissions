class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ["aba","bcb","ece","aa","e"]
        s=set()
        s.add('a')
        s.add('e')
        s.add('i')
        s.add('o')
        s.add('u')
        l=[0]*len(words)
        for i in range(len(words)):
            if words[i][0] in s and words[i][-1] in s :
                l[i]=1
        res=[0]*len(queries)
        for i in range(len(queries)):
            res[i]=sum(l[queries[i][0]:queries[i][1]+1])
        print(l)
        return res
