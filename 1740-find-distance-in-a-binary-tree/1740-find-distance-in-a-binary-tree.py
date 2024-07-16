# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:

        ancestor = None

        def lca(node):

            nonlocal ancestor

            if not node:
                return False
            
            left = lca(node.left)
            right = lca(node.right)

            cur = node.val == p or node.val == q

            if cur + left + right >= 2 and not ancestor:
                ancestor = node
                return True
            
            return cur or left or right
        
        lca(root)
        
        pDist, qDist = 0, 0

        def dfs(node, dist):

            nonlocal pDist, qDist

            if not node:
                return
            
            if node.val == p:
                pDist = dist
            
            if node.val == q:
                qDist = dist
            
            dfs(node.left, dist + 1)
            dfs(node.right, dist + 1)

            return
        
        dfs(ancestor, 0)

        return pDist + qDist