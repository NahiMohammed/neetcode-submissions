class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        has_parent = {}
        nodes = defaultdict(list)
        set_nodes = set()

        for n1, n2 in edges:
            nodes[n1].append(n2)
            nodes[n2].append(n1)   # undirected

            set_nodes.add(n1)
            set_nodes.add(n2)

        # choose 0 as root
        root = 0
        has_parent[root] = None

        visited = set()

        queue = deque([root])

        while queue:
            print(f"queue {queue}, visited = {visited}")

            for _ in range(len(queue)):

                node = queue.popleft()

                if node in visited:
                    return False

                visited.add(node)

                for n in nodes[node]:

                    # n is the parent of node
                    if n == has_parent[node]:
                        continue

                    # n already has a parent -> cycle
                    if n in has_parent:
                        return False

                    has_parent[n] = node
                    queue.append(n)

        return len(visited) == n