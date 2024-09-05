# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        hashMap = collections.defaultdict(list)
        res = []

        def dfs(node):

            if not node:
                return "none"
            
            subtree = ",".join([str(node.val), dfs(node.left), dfs(node.right)])

            if len(hashMap[subtree]) == 1:
                res.append(node)
            hashMap[subtree].append(node)

            return subtree
        
        dfs(root)
        return res
        