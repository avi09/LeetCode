# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
serialized = ""
root = TreeNode(None)
counter = -1
class Codec:

    def serial(root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        global serialized
        serialized += str(root.val) + ";"
        if (not root.left) and (not root.right):
            serialized += "xx;"
        else:
            if root.left:
                Codec.serial(root.left)
            else:
                serialized += "x;"
            if root.right:
                Codec.serial(root.right)
            else:
                serialized += "x;"
        
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        global serialized
        if root == None:
            return ""
        serialized = ""
        Codec.serial(root)
        return serialized
    
    def deserial(data, root):
        global counter
        root.val = int(data[counter])
        counter += 1
        if data[counter] == "xx":
            return
        if not data[counter] == "x":
            root.left = TreeNode(None)
            Codec.deserial(data, root.left)
        counter += 1
        if not data[counter] == "x":
            root.right = TreeNode(None)
            Codec.deserial(data, root.right)
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        global root
        root = TreeNode(None)
        global counter
        counter = 0
        if data == "":
            return None
        data = data[:-1]
        Codec.deserial(data.split(";"), root)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
