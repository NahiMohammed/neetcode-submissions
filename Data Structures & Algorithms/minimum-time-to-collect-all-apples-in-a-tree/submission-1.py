from collections import deque
from typing import List

class TreeNode:
    def __init__(self, val=0, isApple=False):
        self.val = val
        self.children = []
        self.isApple = isApple

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # edges go both ways
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # BFS from 0 to get parents and levels
        parents = {0: None}
        levels = {0: 0}
        queue = deque([0])
        while queue:
            cur = queue.popleft()
            for nxt in graph[cur]:
                if nxt not in parents:
                    parents[nxt] = cur
                    levels[nxt] = levels[cur] + 1
                    queue.append(nxt)

        def lca(n1, n2):
            ancestors = set()
            while n1 is not None:
                ancestors.add(n1)
                n1 = parents[n1]
            while n2 not in ancestors:
                n2 = parents[n2]
            return n2

        def min_distance(n1, n2):
            lowest_common = lca(n1, n2)
            level_lowest = levels[lowest_common]
            return (levels[n1] - level_lowest) + (levels[n2] - level_lowest)

        # build the tree with the real parent/child links
        nodes = [TreeNode(i, isApple=hasApple[i]) for i in range(n)]
        for child in range(1, n):
            nodes[parents[child]].children.append(nodes[child])

        root = nodes[0]
        res = 0
        last = 0

        def dfs(node):
            nonlocal res, last
            if node.isApple:
                res += min_distance(node.val, last)
                last = node.val
            for child in node.children:
                dfs(child)

        dfs(root)
        res += min_distance(last, 0)
        return res