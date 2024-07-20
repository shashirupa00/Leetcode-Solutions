# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        hashMap = {}

        def dfs(node):

            if not node:
                return 
            
            hashMap[node.val] = 1 + hashMap.get(0, node.val)

            dfs(node.left)
            dfs(node.right)

            return
        
        dfs(root)

        for key in hashMap:

            target = k - key

            hashMap[key] -= 1

            if target in hashMap and hashMap[target] - 1:
                return True
            
            hashMap[key] += 1
        
        return False