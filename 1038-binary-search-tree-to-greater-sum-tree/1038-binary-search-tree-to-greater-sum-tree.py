# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        curSum = 0

        def dfs(node):

            nonlocal curSum

            if not node:
                return 
            
            dfs(node.right)

            tempVal = node.val
            node.val += curSum
            curSum += tempVal

            dfs(node.left)

            return 
        
        dfs(root)

        return root