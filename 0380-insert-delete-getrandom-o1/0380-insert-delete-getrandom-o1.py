class RandomizedSet:

    def __init__(self):
        self.nums = set() 

    def insert(self, val: int) -> bool:

        present = val not in self.nums
        self.nums.add(val) 
        return present       

    def remove(self, val: int) -> bool:
        
        present = val in self.nums
        if present: self.nums.remove(val)
        return present
        
    def getRandom(self) -> int:

        curLen = len(self.nums)
        rand = random.randint(0, curLen-1)

        return list(self.nums)[rand]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()