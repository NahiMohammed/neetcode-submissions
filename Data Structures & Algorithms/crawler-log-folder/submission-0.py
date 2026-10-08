class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for f in logs : 
            if f=="../" :
                if stack :
                    stack.pop()
            elif f!="./" :
                stack.append(f)
        return len(stack)
        