# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        if not root:
            return -1
        
        levelSums = []
        deq = collections.deque([root])

        while deq:
            curSum = 0
            for _ in range(len(deq)):

                cur = deq.popleft()
                curSum += cur.val

                if cur.left:
                    deq.append(cur.left)
                
                if cur.right:
                    deq.append(cur.right)
            
            levelSums.append(curSum)

        levelSums.sort()
        return levelSums[-k] if k <= len(levelSums) else -1