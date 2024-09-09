# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        matrix = [[-1 for i in range(n)] for j in range(m)]
        cur = head
        top, down, bottom, up = 0, n - 1, m - 1, 0

        while cur:

            for j in range(up, down + 1):
                matrix[top][j] = cur.val
                cur = cur.next
                if not cur:
                    break
            
            if not cur:
                break

            top += 1
            
            for i in range(top, bottom + 1):
                matrix[i][down] = cur.val
                cur = cur.next
                if not cur:
                    break
            
            if not cur:
                break
            
            down -= 1

            for j in range(down, up - 1, -1):
                matrix[bottom][j] = cur.val
                cur = cur.next
                if not cur:
                    break

            if not cur:
                break
            
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                matrix[i][up] = cur.val
                cur = cur.next
                if not cur:
                    break
            
            if not cur:
                break
            
            up += 1

        return matrix

            
