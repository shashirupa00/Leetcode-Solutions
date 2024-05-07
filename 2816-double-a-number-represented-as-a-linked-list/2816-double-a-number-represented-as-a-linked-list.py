# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:


        def reverse(head):

            prev = None
            cur = head

            while cur:

                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            
            return prev

        head = reverse(head)

        cur = head
        prev = None
        carry = 0

        while cur:

            num = (cur.val * 2) + carry
            carry = 1 if num > 9 else 0

            cur.val = num % 10
            
            prev = cur
            cur = cur.next
            
        
        if carry:
            prev.next = ListNode(1)
        
        return reverse(head)