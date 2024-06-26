# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        res = 0
        
        def dfs(node, p, gp):

            nonlocal res

            if not node:
                return 

            if gp and gp % 2 == 0:
                res += node.val

            dfs(node.left, node.val, p)
            dfs(node.right, node.val, p)

        dfs(root, None, None)

        return res
