# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        minVal, maxVal = min(p.val,q.val), max(p.val,q.val)
        res = 0

        def dfs(node):

            nonlocal res

            if minVal <= node.val and node.val <= maxVal:
                res = node
                return 
            
            elif maxVal < node.val:
                dfs(node.left)
            
            elif minVal > node.val:
                dfs(node.right)
            
            return

        dfs(root)
        return res


        
        