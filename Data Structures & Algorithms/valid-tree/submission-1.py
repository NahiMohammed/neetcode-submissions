class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        has_parent=set()
        nodes=defaultdict(list)
        set_nodes=set()
        for n1 , n2 in edges :
            nodes[n1].append(n2)
            has_parent.add(n2)
            set_nodes.add(n1)
            set_nodes.add(n2)
        if len(has_parent)+1!=len(set_nodes) :
            return False
        root=None
        for n in set_nodes :
            if n  not in has_parent :
                root=n
                break
        visited= set()

        queue=deque([root])
        while queue :
            print(f"queue {queue} , visited = {visited}")
            for _ in range(len(queue)) :
                
                node= queue.popleft()
                
                if node in visited :
                    
                    return False
                else :
                    visited.add(node)
                    for n in nodes[node] :
                        queue.append(n)
        return True

        
        
        
                        

        
        