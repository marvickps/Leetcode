# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        
        if root is None:
            return []

        queue = deque([root])
        res = []

        while queue:
            breadth = []
            breadth_len = len(queue)

            for i in range(breadth_len):
                node = queue.popleft()
                breadth.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            res.append(breadth)
        return res


