# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        val=[]
        def dfs(node):
            
            if not node:
                val.append("Null")
                return
            val.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(val) 
            

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        vals= iter(data.split(","))
        def dfs():
            val= next(vals)
            if val ==  "Null":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node    
        
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))