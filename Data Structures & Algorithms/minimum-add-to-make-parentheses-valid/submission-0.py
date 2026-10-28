class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        res=0
        for c in s :
            if c==')' :
                if stack :
                    stack.pop()
                else :
                    res+=1
                
            if c=="(" :
                stack.append('(')
        return res+ len(stack)
        