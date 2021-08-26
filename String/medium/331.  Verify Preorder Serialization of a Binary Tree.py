class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        idx = 0
        preorder = preorder.split(",")
        
        def DFS(idx): # return end of the subtree idx if subtree is valid, else -1
            if idx >= len(preorder):
                return -1
            
            if preorder[idx] == "#":
                return idx
            
            idx += 1
            left_subtree_end = DFS(idx)
            
            if left_subtree_end < 0:
                return -1
            
            idx = left_subtree_end + 1
            right_subtree_end = DFS(idx)
            
            if right_subtree_end < 0:
                return -1
            
            return right_subtree_end

        return DFS(0) == len(preorder) - 1
            
                