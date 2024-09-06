# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        res = root

        def dfs(node, low, high):
            
            nonlocal res

            if not node:
                return
            
            if not low < p.val < high or not low < q.val < high:
                return
            
            res = node

            dfs(node.left, low, node.val)
            dfs(node.right, node.val, high)

            return
        
        dfs(root, float("-inf"), float("inf"))
        return res