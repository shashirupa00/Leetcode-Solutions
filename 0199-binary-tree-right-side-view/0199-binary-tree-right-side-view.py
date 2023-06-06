# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root: return []

        deq = collections.deque([root])
        res = [root.val]

        while deq:
            for _ in range(len(deq)):

                node = deq.pop()

                if node.right:
                    deq.appendleft(node.right)
                
                if node.left:
                    deq.appendleft(node.left)

            if deq: res.append(deq[-1].val)
        
        return res
        