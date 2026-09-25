# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        #left-root-right
        self.list = []
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            self.list.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return self.list[k-1]

