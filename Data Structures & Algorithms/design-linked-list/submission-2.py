class Node:
    def __init__(self, val=0,next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy = Node()
        self.l = 0
    def printList(self):
        curr = self.dummy.next
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")
        
        

    def get(self, index: int) -> int:
        
        if index>= self.l :
            return -1 
        curr = self.dummy 
        while index :
            curr=curr.next 
            index-=1 
        return curr.next.val
        self.printList()

        

    def addAtHead(self, val: int) -> None:


        after = self.dummy.next 
        self.dummy.next = Node(val , after)
        self.printList()
        self.l +=1
        

    def addAtTail(self, val: int) -> None:
        prev = None 
        curr = self.dummy 
        while curr :
            prev =curr 
            curr= curr.next 
        prev.next = Node(val)
        self.l +=1
        self.printList()
        

    def addAtIndex(self, index: int, val: int) -> None:
        prev = None 
        curr = self.dummy
        while index :
            prev = curr 
            curr = curr.next
            index-=1
        after = curr.next 
        curr.next = Node(val, after)
        self.printList()
        self.l +=1
 

    def deleteAtIndex(self, index: int) -> None:
        if index< self.l :

            curr = self.dummy 
            while index :
                curr = curr.next 
                index-=1
            curr.next= curr.next.next
            self.l -=1
        self.printList()
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)