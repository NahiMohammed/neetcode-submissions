class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        nodes = defaultdict(list)

        for n1, n2 in edges:
            nodes[n1].append(n2)
            nodes[n2].append(n1)

        visited = set()

        queue = deque([(0, -1)])  # (node, parent)
        visited.add(0)

        while queue:
            node, parent = queue.popleft()

            for neighbor in nodes[node]:
                # We found a node we've already visited -> cycle
                if neighbor in visited:
                    return False

                visited.add(neighbor)
                queue.append((neighbor, node))

        # Make sure every node was reached
        return len(visited) == n