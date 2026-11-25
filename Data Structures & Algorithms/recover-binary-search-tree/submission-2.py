class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first = second = prev = None
        current = root

        while current:
            if current.left is None:
                # Visit current
                if prev and prev.val > current.val:
                    if first is None:
                        first = prev
                    second = current

                prev = current
                current = current.right

            else:
                # Find inorder predecessor
                predecessor = current.left

                while (
                    predecessor.right is not None
                    and predecessor.right is not current
                ):
                    predecessor = predecessor.right

                if predecessor.right is None:
                    # Create temporary thread
                    predecessor.right = current
                    current = current.left
                else:
                    # Remove temporary thread and visit current
                    predecessor.right = None

                    if prev and prev.val > current.val:
                        if first is None:
                            first = prev
                        second = current

                    prev = current
                    current = current.right

        first.val, second.val = second.val, first.val