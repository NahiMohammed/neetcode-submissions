# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        paths = {}

        def dfs(node, path):
            if not node:
                return

            path = path + [node]
            paths[node] = path

            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, [])
        lca= root
        for a,b in  zip ( paths[p] ,  paths[q] ) :
            if a==b :
                lca = a 
            else :
                break
            
        return lca






        