# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        res = 0

        def dfs(node):

            nonlocal res

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            res += abs(left) + abs(right)
            node.val += left + right

            return node.val - 1
        
        dfs(root)
        return res