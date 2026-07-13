class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for c in asteroids :
            #print(f"debut satck= {stack}")
            if not stack :
                if c>0:
                    stack.append(c)
            else: 
                last=stack.pop()
                if last*c>0:
                    stack.append(last)
                    stack.append(c)
                else :
                    #print(f"last*c<0 {c}")
                    diff=last+c
                    if diff>0 :
                        stack.append(last)
                    elif diff<0 :
                        stack.append(c)


                    



        return stack
        