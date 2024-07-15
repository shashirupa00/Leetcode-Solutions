# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:

        hashMap = defaultdict(lambda: [None, None])
        children = set()

        for parent, child, isLeft in descriptions:
            
            children.add(child)
            
            if isLeft:
                hashMap[parent][0] = child
            else: