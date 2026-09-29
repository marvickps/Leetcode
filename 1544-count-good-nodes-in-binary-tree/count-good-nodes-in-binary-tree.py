# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs_count(node, maax): 
            if node is None:
                return 0
            if node.val < maax:
                return dfs_count(node.left, maax)+dfs_count(node.right, maax)
            else:
                return 1 + dfs_count(node.left, node.val)+dfs_count(node.right, node.val)
        
        return dfs_count(root,root.val)