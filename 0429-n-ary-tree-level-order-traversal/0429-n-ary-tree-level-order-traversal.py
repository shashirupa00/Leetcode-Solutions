"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        if not root: return []
        
        deq = collections.deque([root])
        res = []

        while deq:
            temp = []
            for _ in range(len(deq)):

                cur = deq.popleft()
                temp.append(cur.val)

                for nxt in cur.children:
                    deq.append(nxt)
            
            res.append(temp)
        
        return res

        