# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        queue = deque([root])
        results = []
        while(len(queue)!=0):
            # print(len(queue))
            
            levels = []
            for _ in range(len(queue)):
                current_node = queue.popleft()
                levels.append(current_node.val)
                if(current_node.left!=None):
                    queue.append(current_node.left)
                if(current_node.right!=None):
                    queue.append(current_node.right)
            results.append(levels)
        print(results)
        return results