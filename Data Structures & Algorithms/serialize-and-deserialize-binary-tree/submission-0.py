# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def preorder(self, root, results):
        if not root:
            results.append("null")
            return
        
        results.append(str(root.val))
        self.preorder(root.left, results)
        self.preorder(root.right, results)

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        # construct the preorder and inorder traversal strings
        results = []
        self.preorder(root, results)

        return ",".join(results)

    def is_number(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        deserialised = [int(x) if self.is_number(x) else x for x in data.split(",")]
        if not deserialised:
            return None
        
        idx = -1

        def traverse():
            nonlocal idx

            idx += 1

            if idx >= len(deserialised):
                return None

            if deserialised[idx] == "null":
                return None
            
            new_node = TreeNode(val=deserialised[idx])
            

            new_node.left = traverse()
            new_node.right = traverse()

            return new_node
        
        return traverse()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))