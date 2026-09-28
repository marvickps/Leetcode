# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        #preorder: 1, 2, 4, 8, 9, 5, 10, 3, 6, 11, 12, 7
                #  0, 1, 2, 3, 4, 5,  6, 7, 8,  9, 10, 11
        #Inorder:  8, 4, 9, 2, 10, 5, 1, 11, 6, 12, 3, 7
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0]) #1
        mid_of_inorder = inorder.index(preorder[0])#6

        root.left = self.buildTree(
            preorder[1:mid_of_inorder+1], #[2,4,8,9,5,10]
            inorder[:mid_of_inorder] #[8,4,9,2,10]
            )        
        root.right = self.buildTree(
            preorder[mid_of_inorder+1:], #[3, 6, 11, 12, 7]
            inorder[mid_of_inorder+1:]   #[11, 6, 12, 3, 7]
        )

        return root