# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:   

        deq = collections.deque([root])
        res = []

        if not root:
            return res

        while deq:
            temp = []
            for _ in range(len(deq)):

                curr = deq.pop()
                temp.append(curr.val)

                if curr.left:
                    deq.appendleft(curr.left)
                
                if curr.right:
                    deq.appendleft(curr.right)

            res.append(temp)

        return res

                