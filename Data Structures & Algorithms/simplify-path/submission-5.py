class Solution:
    def simplifyPath(self, s: str) -> str:
        words = [x for x in s.split("/") if x]
        print(words)
        stack=[]
        for x in words :
            
            if x==".":
                continue
            elif  x=="..":
                if stack :
                    stack.pop()
            else :
                stack.append(x)
        return "/"+"/".join(stack)

         

        