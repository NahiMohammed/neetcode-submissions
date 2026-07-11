class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x=0
        y=0
        s=set()
        s.add((0,0))
        for i in range(len(path)):
            if path[i]=="N":
                y+=1
            elif path[i]=="S":
                y-=1
            elif path[i]=="E":
                x+=1
            else :
                x-=1
            if (x,y) in s :
                return True
            else :
                s.add((x,y))
        return False


        