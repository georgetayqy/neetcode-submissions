# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        print(preorder, inorder)
        
        if len(inorder) == 0:
            return None

        if len(inorder) == 1:
            return TreeNode(val=inorder[0])
        
        top_node = TreeNode(val=preorder[0])
        top_node_index_in_inorder = inorder.index(preorder[0])

        left_inorder = inorder[:top_node_index_in_inorder]
        right_inorder = inorder[top_node_index_in_inorder + 1:]

        top_node.left = self.buildTree(preorder[1:], left_inorder)
        top_node.right = self.buildTree(preorder[1 + len(left_inorder):], right_inorder)

        return top_node
        