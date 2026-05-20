class Solution:
    def getDict(self, temp_list: List[int]) -> dict:
        return {val: i for i, val in enumerate(temp_list)}
        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 1. Build the dictionary once for the entire full list
        inorder_map = self.getDict(inorder)
        
        # 2. Kick off the helper using start/end boundary pointers
        return self.buildTreeHelper(
            preorder, 0, len(preorder) - 1,
            inorder, 0, len(inorder) - 1,
            inorder_map
        )
        
    def buildTreeHelper(self, preorder: List[int], pre_start: int, pre_end: int, 
                       inorder: List[int], in_start: int, in_end: int, 
                       inorder_map: dict) -> Optional[TreeNode]:
        
        # Base case: if pointers cross, this subtree is empty
        if pre_start > pre_end or in_start > in_end:
            return None
            
        # Get the current root value from the preorder start boundary
        root_val = preorder[pre_start]
        root = TreeNode(root_val)
        
        # O(1) dictionary lookup (never breaks because inorder is never sliced)
        index = inorder_map[root_val]
        
        # Exactly equivalent to your previous len(left_subtree_in)
        left_subtree_len = index - in_start
        
        # 3. Recurse into subtrees by updating boundary coordinates
        root.left = self.buildTreeHelper(
            preorder, pre_start + 1, pre_start + left_subtree_len,
            inorder, in_start, index - 1,
            inorder_map
        )
        
        root.right = self.buildTreeHelper(
            preorder, pre_start + left_subtree_len + 1, pre_end,
            inorder, index + 1, in_end,
            inorder_map
        )
        
        return root
