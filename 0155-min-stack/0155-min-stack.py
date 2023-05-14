class MinStack:

    def __init__(self):
        self.deq = collections.deque()
        self.minVal = collections.deque()   

    def push(self, val: int) -> None:
        self.deq.append(val)
        if len(self.minVal) == 0 or self.minVal[-1] >= val:
            self.minVal.append(val)   

    def pop(self) -> None:
        n = self.deq.pop() 
        if self.minVal[-1] == n:
            self.minVal.pop()     

    def top(self) -> int:
        return self.deq[-1]        

    def getMin(self) -> int:
        return int(self.minVal[-1])
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()