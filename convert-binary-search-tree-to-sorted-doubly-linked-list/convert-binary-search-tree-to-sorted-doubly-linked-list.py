"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root: return None
        
        res = []

        def dfs(node):
            
            if not node:
                return
            
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)

        head = Node(-1)
        cur = head

        for i, num in enumerate(res):
            cur.right = Node(num, cur)
            cur = cur.right

        cur.right = head.right
        head.right.left = cur

        return head.right

        
        