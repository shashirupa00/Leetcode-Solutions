# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        cur = head
        arr = []

        while cur:
            arr.append(cur.val)
            cur = cur.next
        
        n = len(arr)
        extras, averageSize = n % k, n // k
        res = []
        start = 0

        if n < k:
            extras, averageSize = 0, 1

        while start < len(arr):
            end = start + averageSize + 1 if extras else start + averageSize
            res.append(arr[start:end])
            start = end
            if extras: extras -= 1
        
        if n < k:
            while n < k:
                res.append([])
                n += 1
        
        def convertToLinkedList(arr):
            if not arr:
                return None
            head = ListNode(arr[0])
            cur = head
            for i in range(1, len(arr)):
                cur.next = ListNode(arr[i])
                cur = cur.next
            return head
        
        for i in range(len(res)):
            res[i] = convertToLinkedList(res[i])

        return res