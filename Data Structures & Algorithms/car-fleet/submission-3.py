class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        res=0
        stack=[]
        for i in range(len(pairs)) :
            time=(target-pairs[i][0])/pairs[i][1]

            if not stack :
                stack.append(time)
                
            else :
                
                
                if time > stack[-1]: 
                    stack.append(time)

        return len(stack)
        
        