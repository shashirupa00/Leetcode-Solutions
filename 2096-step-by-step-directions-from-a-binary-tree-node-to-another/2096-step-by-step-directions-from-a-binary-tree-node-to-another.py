# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        ancestor = None

        def lca(node):
            
            nonlocal ancestor

            if not node:
                return False

            left = lca(node.left)
            right = lca(node.right)

            cur = False
            if node.val == startValue or node.val == destValue:
                cur = True

            if left + cur + right >= 2 and not ancestor:
                ancestor = node
        
            return cur or left or right
        
        lca(root)

        print(ancestor.val)
        
        sourcePath = ""
        destPath = ""

        def dfs(node, path, target):

            nonlocal sourcePath, destPath

            if not node: return

            if node.val == target:
                if target == startValue:
                    sourcePath = path
                else:
                    destPath = path
                return
            
            dfs(node.left, path + "L", target)
            dfs(node.right, path + "R", target)

            return path

        dfs(ancestor, "", startValue)
        dfs(ancestor, "", destValue)

        startPath = "U" * len(sourcePath)

        return startPath + destPath