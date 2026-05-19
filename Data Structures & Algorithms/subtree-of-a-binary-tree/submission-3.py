# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def search(self, current_node, value):
        print("current_node.val, value",current_node.val, value)
        if(current_node == None):
            return None
        if (value==current_node.val):
            return current_node
        if(value<current_node.val):
            return self.search(current_node.left, value)
        else:
            return self.search(current_node.right, value)

    def isSame(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if(p == None and q==None):
            return True
        if(p!= None and q==None):
            return False
        if(p==None and q!=None):
            return False
        if(p.val==q.val) and self.isSame(p.left,q.left) and self.isSame(p.right,q.right):
            return True
        return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # we need to find pointer to subroot in main tree. And then we can comare the both subtrees
        if root == None:
            return False

        if (self.isSame(root, subRoot)):
            return True
        if(self.isSubtree(root.left, subRoot)) or (self.isSubtree(root.right, subRoot)):
            return True
        return False