# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def findGcd(num1, num2):

            if num1 < num2:
                num1, num2 = num2, num1
            
            res = 1
            
            for i in range(1, num2 + 1):
                if num2 % i == 0 and num1 % i == 0:
                    res = i
            
            return res
        
        cur = head

        while cur and cur.next:
            n1, n2 = cur.val, cur.next.val
            gcd = findGcd(n1, n2)
            nxt = cur.next
            cur.next = None
            cur.next = ListNode(gcd, nxt)
            cur = nxt
        
        return head
