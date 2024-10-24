class ListNode:

    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = ListNode(-1, -1), ListNode(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self, node):
        
        prevNode, nxtNode = node.prev, node.next 
        prevNode.next, nxtNode.prev = nxtNode, prevNode

    def insert(self, node):

        prevNode, nxtNode = self.tail.prev, self.tail
        prevNode.next, nxtNode.prev = node, node
        node.prev, node.next = prevNode, nxtNode

    def get(self, key: int) -> int:
        
        if key not in self.cache:
            return -1
        
        res = self.cache[key].val

        self.remove(self.cache[key])
        self.insert(self.cache[key])

        return res

    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]
        elif len(self.cache) >= self.capacity:
            lru_node = self.head.next
            self.remove(lru_node)
            del self.cache[lru_node.key]
        
        new_node = ListNode(key, value)
        self.insert(new_node)
        self.cache[key] = new_node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)