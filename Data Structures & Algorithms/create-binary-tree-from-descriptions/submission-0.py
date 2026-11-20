class Solution:
    def createBinaryTree(self, descriptions):
        dic = {}
        childs = set()

        for parent, child, isleft in descriptions:
            if parent not in dic:
                dic[parent] = TreeNode(parent)

            if child not in dic:
                dic[child] = TreeNode(child)

            childs.add(child)

            if isleft:
                dic[parent].left = dic[child]
            else:
                dic[parent].right = dic[child]

        for node in dic:
            if node not in childs:
                return dic[node]

        return None