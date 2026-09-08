class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr=set()
        res=0
        idx=deque()
        for i,c in enumerate(s) :
            if c not in curr :
                curr.add(c)
                idx.append(i)
                res=max(res,len(curr))
            else :
                while s[i] in curr :
                    id= idx.popleft()
                    curr.remove(s[id])


        return res
        