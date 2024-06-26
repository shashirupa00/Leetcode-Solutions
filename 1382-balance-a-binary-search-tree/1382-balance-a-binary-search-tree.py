# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        arr = []

        def dfs(node):

            if not node:
                return
            
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

            return

        dfs(root)

        def createTree(start, end):

            if start > end:
                return

            pos = (start + end) // 2

            if start == end:
                return TreeNode(arr[pos])
            
            cur = TreeNode(arr[pos])

            cur.left = createTree(start, pos-1)
            cur.right = createTree(pos+1, end)

            return cur
        
        return createTree(0, len(arr)-1)        