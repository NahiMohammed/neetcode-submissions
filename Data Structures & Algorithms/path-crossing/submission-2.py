class Solution:
    def isPathCrossing(self, path: str) -> bool:
        def update(cor,d) : 
            match d:
                case 'N':
                    return (cor[0]+1,cor[1])
                case 'S':
                    return (cor[0]-1,cor[1])
                case 'E':
                    return (cor[0],cor[1]+1)
                case 'W':
                    return (cor[0],cor[1]-1)

            return cor
        prev=set()
        prev.add((0,0))
        curr=[0,0]
        for c in path :
            new = update(curr,c)
            if new in prev :
                return True 
            prev.add(new)
            curr=new
        return False


        