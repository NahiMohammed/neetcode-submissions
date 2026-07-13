class Solution:
    def simplifyPath(self, s: str) -> str:
        words = [x for x in s.split("/") if x]
        stack=[]
        for x in words :
            if x[0]==".":
                continue
            elif  x[0]=="..":
                if stack :
                    stack.pop()
            else :
                stack.append(x)
        return "/"+"/".join(stack)

         

        