"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        hashMap = {}

        def dfs(node):

            if node in hashMap:
                return hashMap[node]
            
            copy = Node(node.val)
            hashMap[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))
            return copy
        
        return None if not node else dfs(node) 

