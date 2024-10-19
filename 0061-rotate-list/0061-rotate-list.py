# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not k or not head.next:
            return head
        
        length = 0
        cur = head

        while cur:
            length += 1
            cur = cur.next
        
        if length == k:
            return head
        
        k = k % length
        cur = head
        curLength = 0

        if not k:
            return head
            
        while curLength < length - k - 1:

            curLength += 1
            cur = cur.next
        
        tempHead = cur.next
        cur.next = None

        curTemp = tempHead

        while curTemp.next:
            curTemp = curTemp.next
        
        curTemp.next = head

        return tempHead



        