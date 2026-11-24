class TreeNode :
    def __init__(self , val  =  0 , manage =None , informTime = 0 ) -> None:
        self.val =val 
        self.manage = manage  if manage is not None else []
        self.informTime = informTime
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        trees = [TreeNode(i) for i in range(n)]
        for i , v in enumerate(manager) :
            if v == -1 :
                trees[headID].informTime=informTime[i]
            else :
                trees[v].manage.append(trees[i])
                trees[i].informTime = informTime[i]
        q= deque([(trees[headID],0)])
        res = 0

        while q :
            
            node,time = q.popleft()
            res = max(res,time + node.informTime)
            if node.manage :
                for n in node.manage :
                    q.append((n,time + node.informTime))

        return res



    
