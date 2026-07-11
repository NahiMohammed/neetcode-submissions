class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res=[]
        def isSubstring(s1, s2):
            if len(s1) >= len(s2):
                return False

            for i in range(len(s2) - len(s1) + 1):
                j = 0
                while j < len(s1) and s2[i + j] == s1[j]:
                    j += 1
                if j == len(s1):
                    return True

            return False

        for w in words :
            for w1 in words :
                if isSubstring(w,w1):

                    res.append(w)
        return res

        