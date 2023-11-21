# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root: return []
        
        hashMap = collections.defaultdict(list)
        deq = collections.deque([(root, 0)])
        res = []

        while deq:
            for _ in range(len(deq)):

                cur, col = deq.popleft()

                hashMap[col].append(cur.val)

                if cur.left:
                    deq.append((cur.left, col-1))

                if cur.right:
                    deq.append((cur.right, col+1))
        
        low, high = min(hashMap), max(hashMap)

        for i in range(low, high+1):
            res.append(hashMap[i])

        return res