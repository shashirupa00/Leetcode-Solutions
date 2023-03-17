# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root == None: return 0
        
        visited = set()
        q =collections.deque([root])
        depth = 0

        while q:

            for _ in range(len(q)):

                curr = q.pop()
                visited.add(curr)

                if curr.right and curr.right not in visited:
                    q.appendleft(curr.right)

                if curr.left and curr.left not in visited:
                    q.appendleft(curr.left)

            depth += 1

        return depth




        