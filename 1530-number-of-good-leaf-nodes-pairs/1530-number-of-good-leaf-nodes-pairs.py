# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        hashMap = defaultdict(list)
        leafNodes = []

        def dfs(node):
            
            if not node:
                return

            if not node.left and not node.right:
                leafNodes.append(node)
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left:
                hashMap[left].append(node)
                hashMap[node].append(left)
            if right:
                hashMap[right].append(node)
                hashMap[node].append(right)
            
            return node
        
        dfs(root)

        visited = set()
        res = 0

        def dfs2(node, dist):

            nonlocal res
            
            visited.add(node)

            for nxt in hashMap[node]:
                if nxt not in visited and dist + 1 <= distance:
                    dfs2(nxt, dist + 1)
                    if not nxt.left and not nxt.right:
                        print("child", nxt.val)
                        res += 1
            
            return
        
        for node in leafNodes:
            print("parent", node.val)
            visited = set()
            dfs2(node, 0)
        
        return res // 2