# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root: return []
        
        deq = collections.deque([root])
        res = []

        while deq:
            tempLevel = []
            for i in range(len(deq)):

                cur = deq.popleft()

                tempLevel.append(cur.val)

                if cur.left:
                    deq.append(cur.left)
                
                if cur.right:
                    deq.append(cur.right)
            
            res.append(tempLevel)
        
        return res
