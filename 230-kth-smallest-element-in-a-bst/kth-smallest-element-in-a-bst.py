# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        #left-root-right
        self.temp_k =0
        self.res = None

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            if self.res is not None:
                return
            self.temp_k+=1
            if self.temp_k == k:
                self.res = node.val
                return
            
            inorder(node.right)

        inorder(root)

        return self.res
        

