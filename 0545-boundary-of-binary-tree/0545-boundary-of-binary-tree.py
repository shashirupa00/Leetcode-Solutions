# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        
        left, leafs, right = [], [], []

        def leftDfs(node):
            
            if not node or not node.left and not node.right:
                return
            
            left.append(node.val)

            if node.left:
                leftDfs(node.left)
            
            elif node.right:
                leftDfs(node.right)
            
            return


        def leafsDfs(node):

            if not node:
                return
            
            leafsDfs(node.left)

            if node != root and not node.left and not node.right:
                
                leafs.append(node.val)

            leafsDfs(node.right)
            
            return node.val
        

        def rightDfs(node):
            
            if not node or not node.left and not node.right:
                return
            
            if node.right:
                rightDfs(node.right)
            
            elif node.left:
                rightDfs(node.left)
            
            right.append(node.val)

            return

        leftDfs(root.left)
        leafsDfs(root)
        rightDfs(root.right)

        print(left, leafs, right)

        return [root.val] + left + leafs + right