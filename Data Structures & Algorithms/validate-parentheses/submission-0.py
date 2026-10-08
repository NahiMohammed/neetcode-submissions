class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        open=['(','[','{']
        opposite={'(':')','[':']','{':'}'}
        for c in s  :
            if c in open  :
                stack.append(c)
            else : 
                if not stack :
                    return False
                else :
                    last=stack.pop()
                    if opposite[last]!=c :
                        return False 
        return not stack

        