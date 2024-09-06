# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        res = [root.val]
        deq = collections.deque([root])

        while deq:
            for _ in range(len(deq)):

                cur = deq.popleft()

                if cur.left:
                    deq.append(cur.left)
                
                if cur.right:
                    deq.append(cur.right)
            
            if deq:
                res.append(deq[-1].val)
        
        return res