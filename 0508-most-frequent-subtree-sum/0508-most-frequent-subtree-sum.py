# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        hashMap = defaultdict(int)
        maxFreq = 0
        res = []

        def dfs(node):

            nonlocal maxFreq

            if not node:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)

            curSum = node.val + l + r

            hashMap[curSum] += 1
            maxFreq = max(maxFreq, hashMap[curSum])

            return curSum
        
        dfs(root)

        for s, f in hashMap.items():
            if f == maxFreq: res.append(s)
        
        return res

