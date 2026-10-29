class FreqStack:

    def __init__(self):
        self.st = []
        self.fr = defaultdict(int)
        
        
        

    def push(self, val: int) -> None:
        self.st.append(val)
        self.fr[val]+=1
        

        

    def pop(self) -> int:
        max_fr = max(self.fr.values())
        i = len(self.st)-1
        while self.fr[self.st[i]]!=max_fr :
            i-=1
        self.fr[self.st[i]]-=1
        return self.st.pop(i)

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()