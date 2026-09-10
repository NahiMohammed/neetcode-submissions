class Node:
    def __init__(self, val, min_val):
        self.val = val
        self.min_val = min_val
        self.next = None


class MinStack:

    def __init__(self):
        self.head = None

    def push(self, val: int) -> None:
        if self.head is None:
            node = Node(val, val)
        else:
            node = Node(val, min(val, self.head.min_val))

        node.next = self.head
        self.head = node

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.min_val