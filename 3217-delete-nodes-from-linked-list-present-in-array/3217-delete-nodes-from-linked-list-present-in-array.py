# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = ListNode(None, head)
        cur = prev
        nums = set(nums)

        while cur:
            while cur.next and cur.next.val in nums:
                cur.next = cur.next.next
            cur = cur.next
        
        return prev.next