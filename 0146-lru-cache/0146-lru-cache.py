class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):

        self.cap = capacity
        self.cache = {}

        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, Node):
        prevNode, nxtNode = Node.prev, Node.next
        prevNode.next, nxtNode.prev = nxtNode, prevNode
        
    def insert(self, Node):
        prevNode, nxtNode = self.right.prev, self.right
        prevNode.next, nxtNode.prev = Node, Node
        Node.prev, Node.next = prevNode, nxtNode

    def get(self, key: int) -> int:

        if key in self.cache:

            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val
        
        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])

        else:
            self.cache[key] = Node(key, value)
        
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            del self.cache[self.left.next.key]
            self.remove(self.left.next)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)