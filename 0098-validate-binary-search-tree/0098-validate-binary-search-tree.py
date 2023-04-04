# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, minLeft, maxRight):

            if not node:
                return True

            if node.val <= minLeft or node.val >= maxRight:
                return False
      
            return (dfs(node.left, minLeft, node.val) and dfs(node.right, node.val, maxRight))
       
        return dfs(root, float("-inf"), float("inf"))
        


        