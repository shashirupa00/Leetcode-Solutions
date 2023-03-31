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

        deq = collections.deque([root])
        res = []

        while deq:
            
            for _ in range(len(deq)):

                curr = deq.pop()
                
                if curr.left:
                    deq.appendleft(curr.left)

                if curr.right:
                    deq.appendleft(curr.right)

            res.append(curr.val)

        return res


  

