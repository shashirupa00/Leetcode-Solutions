# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        deq = collections.deque([root])
        res = []

        if not root: return res

        while deq:
            tmp = []
            for _ in range(len(deq)):
                
                node = deq.pop()
                tmp.append(node.val)

                if node.left:
                    deq.appendleft(node.left)
                
                if node.right:
                    deq.appendleft(node.right)
            
            res.append(tmp)
        
        return res


        