class MyQueue:

    def __init__(self):
        self.st1=[]
        self.st2=[]
        

    def push(self, x: int) -> None:
        self.st2.append(x)
        while self.st1 :
            self.st2.append(self.st1.pop())
        self.st1,self.st2=self.st2,self.st1

        

    def pop(self) -> int:
        return self.st1.pop()
        

    def peek(self) -> int:
        return self.st1[-1]
        

    def empty(self) -> bool:
        return len(self.st1)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()