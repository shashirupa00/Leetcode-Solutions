# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        tmp1, tmp2 = list1, list2
        head = ListNode(None)
        tmp = head

        while tmp1 and tmp2:
            if tmp1.val >= tmp2.val:
                head.next = tmp2
                tmp2 = tmp2.next
            
            else:
                head.next = tmp1
                tmp1 = tmp1.next
            
            head = head.next
        
        if tmp1:
            head.next = tmp1
        
        if tmp2:
            head.next = tmp2
        
        return tmp.next
        
        



        