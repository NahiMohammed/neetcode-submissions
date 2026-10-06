class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        split=s.split(" ")
        if len(split)!=len(pattern) :
            return False
        dic ={}
        dic2 = {}
        for i in range(len(pattern)) :
            if pattern[i]  in dic :
                if dic[pattern[i]]!=split[i]:
                    return False
            else :
                dic[pattern[i]]=split[i]
            if split[i]  in dic2 :
                if dic2[split[i]]!=pattern[i]:
                    return False
            else :
                dic2[split[i]]=pattern[i]
        return True
        