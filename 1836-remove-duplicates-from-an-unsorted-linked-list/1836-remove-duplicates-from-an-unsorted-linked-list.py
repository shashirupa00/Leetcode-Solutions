# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        
        hashMap = {}
        cur = head

        while cur:
            hashMap[cur.val] = 1 + hashMap.get(cur.val, 0)
            cur = cur.next
        
        cur = head
        prev = ListNode()
        newHead = prev
        
        while cur:

            while cur and hashMap[cur.val] > 1:
                cur = cur.next
            
            prev.next = cur
            prev = prev.next
            if cur: cur = cur.next
        
        return newHead.next