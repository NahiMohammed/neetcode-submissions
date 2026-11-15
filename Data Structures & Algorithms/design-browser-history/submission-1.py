class Node:
    def __init__(self, val="", next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)

    def visit(self, url: str) -> None:
        new = Node(url)
        self.curr.next = new
        new.prev = self.curr
        self.curr = new

    def back(self, steps: int) -> str:
        while steps > 0 and self.curr.prev:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.curr.next:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val