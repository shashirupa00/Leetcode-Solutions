# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        def initial_deque():
            return deque([(-1, -1), (-1, -1)])

        hashMap = defaultdict(initial_deque)

        def dfs(node, level):

            if not node:
                return 0
            
            l = dfs(node.left, level + 1)
            r = dfs(node.right, level + 1)

            curHeight = max(l, r)
           
            if curHeight > hashMap[level][0][0]:
                hashMap[level].pop()
                hashMap[level].appendleft([curHeight, node.val])
            elif curHeight > hashMap[level][1][0]:
                hashMap[level].pop()
                hashMap[level].append([curHeight, node.val])
            
            return curHeight + 1
        
        dfs(root, 0)
        treeHeight = hashMap[0][0][0]

        heightMap = {}

        for level in hashMap:
            height, node = hashMap[level][0][0], hashMap[level][0][1]
            nxtHeight = hashMap[level][1][0]
            heightMap[node] = treeHeight - height + nxtHeight
        
        res = []

        for node in queries:
            if node in heightMap:
                res.append(heightMap[node])
            else:
                res.append(treeHeight)

        return res
            
