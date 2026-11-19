class Node:
    def __init__(self, key=0, val=0, frequency=1, next=None, prev=None):
        self.key = key
        self.val = val
        self.f = frequency
        self.prev = prev
        self.next = next


class LFUCache:

    def __init__(self, capacity: int):
        self.right = Node()
        self.left = Node()
        self.right.prev = self.left
        self.left.next = self.right
        self.dic = {}
        self.capacity = capacity

    def delete(self, node: Node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.delete(node)
            self.insert(node)          # now the most recently used
            node.f += 1
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.dic:
            node = self.dic[key]
            node.val = value
            self.delete(node)
            self.insert(node)
            node.f += 1
            return

        if len(self.dic) >= self.capacity:
            # find the minimum frequency
            # (strict "<" keeps the oldest node when there is a tie)
            lfu = self.left.next
            cur = lfu.next
            while cur != self.right:
                if cur.f < lfu.f:
                    lfu = cur
                cur = cur.next
            self.delete(lfu)
            del self.dic[lfu.key]

        node = Node(key, value)
        self.dic[key] = node
        self.insert(node)


        