# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        arr = []

        def dfs(node):

            if not node:
                arr.append("N")
                return

            arr.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return " ".join(str(arr[i]) for i in range(len(arr)))    
        

    def deserialize(self, data):

        nums = data.split(" ")
        self.i = 0

        def dfs():

            if nums[self.i] == 'N':
                self.i += 1
                return
            
            node = TreeNode(int(nums[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()




        



        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))