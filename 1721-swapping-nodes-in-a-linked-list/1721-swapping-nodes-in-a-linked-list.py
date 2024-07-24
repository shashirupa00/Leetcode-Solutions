# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        length = 0
        cur = head

        while cur:
            cur = cur.next
            length += 1

        p = length - k + 1
        cur = head
        pos = 1
        node1, node2 = -1, -1

        while cur:
            if pos == k:
                node1 = cur
            if pos == p:
                node2 = cur
            pos += 1
            cur = cur.next

        node1.val, node2.val = node2.val, node1.val

        return head
