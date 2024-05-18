class MRUQueue:

    def __init__(self, n: int):

        self.deq = collections.deque([i+1 for i in range(n)])
          
    def fetch(self, k: int) -> int:

        if k == len(self.deq):
            return self.deq[-1]

        temp = []

        while k > 1:
            temp.append(self.deq.popleft())
            k -= 1
        
        num = self.deq.popleft()

        for n in reversed(temp):
            self.deq.appendleft(n)
        
        self.deq.append(num)

        return num

        


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)