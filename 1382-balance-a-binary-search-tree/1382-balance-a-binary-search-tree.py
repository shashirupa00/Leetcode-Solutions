# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        inOrder = []

        def dfs(node):
            
            if not node:
                return
            
            dfs(node.left)
            inOrder.append(node.val)
            dfs(node.right)
        
        dfs(root)
        
        def buildTree(low, high):

            if low >= high:
                return None
            
            mid = (low + high) // 2
            curNode = TreeNode(inOrder[mid])

            curNode.left = buildTree(low, mid)
            curNode.right = buildTree(mid + 1, high)

            return curNode
        
        return buildTree(0, len(inOrder))