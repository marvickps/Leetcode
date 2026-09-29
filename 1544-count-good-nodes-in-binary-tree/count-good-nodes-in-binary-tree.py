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
            count = 0
            maax = max(maax, node.val)
            if maax <= node.val:
                count =1
            # if node.val>= maax:
            #     count = 1
            


            count += dfs_count(node.left, maax)
            count += dfs_count(node.right, maax)

            return count

        
        return dfs_count(root, root.val)
            
        