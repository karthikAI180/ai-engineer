class FreqStack:

    def __init__(self):
        self.cnt = {}
        self.stacks = {}
        self.max_count=0
        
    def push(self, val: int) -> None:
        value=self.cnt.get(val,0)+1
        self.cnt[val] = value
        if self.max_count<value:
            self.max_count=value
            self.stacks[value]=[]
        self.stacks[value].append(val)
        
    def pop(self) -> int:
        res=self.stacks[self.max_count].pop()
        self.cnt[res]-=1
        if not self.stacks[self.max_count]:
            self.max_count-=1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()