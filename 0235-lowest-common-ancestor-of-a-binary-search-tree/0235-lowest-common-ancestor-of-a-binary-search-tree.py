# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        res = root

        def dfs(node, left, right):
            
            nonlocal res

            if not node:
                return
            
            if not left < p.val < right or not left < q.val < right:
                return
            
            res = node

            dfs(node.left, left, node.val)
            dfs(node.right, node.val, right)

            return
        
        dfs(root, float("-inf"), float("inf"))
        return res