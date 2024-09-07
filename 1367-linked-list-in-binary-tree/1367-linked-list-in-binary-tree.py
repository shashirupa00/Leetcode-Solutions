# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        cur = head
        res = False

        def dfs(node, cur):
            
            nonlocal res

            if not node:
                return
            
            if node.val == cur.val:
                cur = cur.next
                if not cur:
                    res = True
                    return
            
            dfs(node.left, cur)
            dfs(node.right, cur)

            return

        dfs(root, cur)
        return res