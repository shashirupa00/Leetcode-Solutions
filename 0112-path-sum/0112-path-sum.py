# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        res = False
        
        def dfs(node, curSum):
            
            nonlocal res

            if not node:
                return

            curSum += node.val

            if curSum == targetSum and node.left == None and node.right == None:
                res = True
            
            dfs(node.left, curSum)
            dfs(node.right, curSum)

            return
        
        dfs(root, 0)
        return res