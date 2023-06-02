class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hashMap = {}

        self.head, self.tail = Node(0,0), Node(0,0)

        #   head -> Most recently used, tail -> LRU
        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prv, nxt = self.tail.prev, self.tail
        prv.next = nxt.prev = node
        node.next, node.prev = nxt, prv

    def get(self, key: int) -> int:
        if key in self.hashMap:
            self.remove(self.hashMap[key])
            self.insert(self.hashMap[key])            
            return self.hashMap[key].val    
        return -1        

    def put(self, key: int, value: int) -> None:

        if key in self.hashMap:
            self.remove(self.hashMap[key])
        self.hashMap[key] = Node(key, value)
        self.insert(self.hashMap[key])

        if len(self.hashMap) > self.cap:
            node = self.head.next
            self.remove(node)
            del self.hashMap[node.key]

            

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)