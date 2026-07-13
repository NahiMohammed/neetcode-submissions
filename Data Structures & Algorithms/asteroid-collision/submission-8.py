class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for c in asteroids :
            #print(f"debut satck= {stack}")
            if not stack or stack[-1]*c>0:
                    stack.append(c)
            else :
                flag=True
                while stack and stack[-1]+c <=0 and flag:
                    if stack[-1]+c==0 :
                        flag=False
                    stack.pop()

                    
                if not stack and flag :
                    stack.append(c)


            

        return stack
        