# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        res = []

        def dfs(node):

            res.append(str(node.val) if node else 'N')

            if not node:
                return
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        data = data.split(',')
        i = 0

        def dfs():

            nonlocal i
            
            if data[i] == 'N':
                i += 1
                return None
            
            cur = TreeNode(int(data[i]))
            i += 1
            cur.left = dfs()
            cur.right = dfs()

            return cur

        
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))