class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        nodes = defaultdict(list)

        for n1, n2 in edges:
            nodes[n1].append(n2)
            nodes[n2].append(n1)

        visited = set()

        queue = deque([(0, -1)])  
        visited.add(0)
        while queue:
            node, parent = queue.popleft()

            for neighbor in nodes[node]:

                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False

                visited.add(neighbor)
                queue.append((neighbor, node))

        return len(visited) == n