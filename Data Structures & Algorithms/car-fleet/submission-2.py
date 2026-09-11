class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        indices = sorted(range(len(position)), key=lambda i: position[i],  reverse=True)
        for i in indices :
            t = (target-position[i])/speed[i]
            if not stack or stack[-1]<t:
                stack.append(t)
        return len(stack)

                



        