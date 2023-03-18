# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        deq = collections.deque([(p,q)])

        while deq:

            for _ in range(len(deq)):

                curr1, curr2 = deq.pop()

                if not curr1 and not curr2:
                    continue

                if not curr1 or not curr2:
                    return False
                
                if curr1.val != curr2.val:
                    return False

                deq.appendleft([curr1.left, curr2.left])
                deq.appendleft([curr1.right, curr2.right])

        return True