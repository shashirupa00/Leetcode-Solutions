# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        zeroCount = 0
        curSum = 0
        resHead = ListNode()
        resCur = resHead
        cur = head

        while cur:

            if cur.val == 0:
                zeroCount += 1
            
            curSum += cur.val

            if zeroCount == 2:
                resCur.next = ListNode(curSum, None)
                resCur = resCur.next
                zeroCount = 1
                curSum = 0
            
            cur = cur.next
        
        return resHead.next
