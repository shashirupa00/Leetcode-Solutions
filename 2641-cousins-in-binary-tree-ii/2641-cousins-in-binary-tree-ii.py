# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        levelSums = defaultdict(list)
        levelSums[0].append((root.val, root, None))

        def dfs(node, level):

            if not node:
                return
            
            if node.left or node.right:
                curSum = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
                levelSums[level + 1].append((curSum, (node.left if node.left else None), (node.right if node.right else None)))

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            
            return
        
        dfs(root, 0)

        for level in levelSums:
            curLevelSum = sum([l[0] for l in levelSums[level]])
            for nodes in levelSums[level]:

                node1 = nodes[1] if nodes[1] else None
                node2 = nodes[2] if nodes[2] else None

                if node1: node1.val = curLevelSum - nodes[0]
                if node2: node2.val = curLevelSum - nodes[0]
        
        return root
