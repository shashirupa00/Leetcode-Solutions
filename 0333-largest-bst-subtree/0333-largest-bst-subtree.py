# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class NodeValue:
    def __init__(self, minVal, maxVal, totalNodes):
        self.minVal = minVal
        self.maxVal = maxVal
        self.totalNodes = totalNodes

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        
        res = 0

        def dfs(node):

            nonlocal res

            if not node:
                return NodeValue(float("inf"), float("-inf"), 0)
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left.maxVal < node.val < right.minVal:
                return NodeValue(min(left.minVal, node.val), max(right.maxVal, node.val), 1 + left.totalNodes + right.totalNodes)
            
            return NodeValue(float("-inf"), float("inf"), max(left.totalNodes, right.totalNodes))
        
        return dfs(root).totalNodes