# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def has_duplicates(self, my_list):
        return len(my_list) != len(set(my_list))    
    def in_order(self, root: Optional[TreeNode]) ->list:
        results = []
        def traverse(current_node):
            if current_node.left:
                traverse(current_node.left)
            results.append(current_node.val)
            if current_node.right:
                traverse(current_node.right)
            return results
        return traverse(root)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        results = self.in_order(root)
        sorted_results = sorted(results)
        if(self.has_duplicates(results)):
            return False
        if(results == sorted_results):
            return True
        
        else:
            return False