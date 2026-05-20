class Solution:
    def getDict(self, temp_list: List[int]) -> dict:
        return {val: i for i, val in enumerate(temp_list)}
        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        # Build the map once at the very top level
        inorder_map = self.getDict(inorder)
        # Pass the initial full boundaries of the arrays
        return self.buildTreeHelper(preorder, 0, len(preorder) - 1, 
                                    inorder, 0, len(inorder) - 1, 
                                    inorder_map)
    
    def buildTreeHelper(self, preorder: List[int], pre_start: int, pre_end: int, 
                       inorder: List[int], in_start: int, in_end: int, 
                       inorder_map: dict) -> Optional[TreeNode]:
        
        # Base case: if pointers cross, this subtree segment is empty
        if pre_start > pre_end or in_start > in_end:
            return None
            
        root_val = preorder[pre_start]
        root = TreeNode(root_val)
        
        # O(1) index lookup works perfectly because arrays are never sliced
        index = inorder_map[root_val]
        left_len = index - in_start
        
        # Move pointers inward on the original full arrays
        root.left = self.buildTreeHelper(
            preorder, pre_start + 1, pre_start + left_len,
            inorder, in_start, index - 1,
            inorder_map
        )
        root.right = self.buildTreeHelper(
            preorder, pre_start + left_len + 1, pre_end,
            inorder, index + 1, in_end,
            inorder_map
        )
        
        return root
