class TimeMap:

    def __init__(self):
        self.valueMap = collections.defaultdict(list)
        self.timeMap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.valueMap[key].append(value)
        self.timeMap[key].append(timestamp)
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""

        nums = self.timeMap[key]
        l, r= 0, len(nums)-1
        res = ""

        while l<=r:

            mid = (l+r)//2

            if nums[mid] <= timestamp:
                res = mid 
                l = mid + 1
            
            else:
                if timestamp < nums[mid]:
                    r = mid - 1        
                else:
                    l = mid+1
        
        return "" if res == "" else self.valueMap[key][res]        



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)