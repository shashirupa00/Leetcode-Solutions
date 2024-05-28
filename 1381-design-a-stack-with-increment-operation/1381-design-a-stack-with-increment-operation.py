class CustomStack:

    def __init__(self, maxSize: int):

        self.n = maxSize
        self.arr = []        

    def push(self, x: int) -> None:

        if len(self.arr) < self.n:
            self.arr.append(x)                                

    def pop(self) -> int:

        num = -1
        
        if self.arr: num = self.arr.pop()
        
        return num 
        
    def increment(self, k: int, val: int) -> None:

        for i in range(k):
            if i < len(self.arr):
                self.arr[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)