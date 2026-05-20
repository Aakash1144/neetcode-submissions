# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def in_order(self, root: Optional[TreeNode]) -> list:
        results = []
        def traverse(current_node):
            if(current_node.left):
                traverse(current_node.left)
            results.append(current_node.val)
            if(current_node.right):
                traverse(current_node.right)
            return results
        return traverse(root)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return None
        results = self.in_order(root)
        return results[k-1]