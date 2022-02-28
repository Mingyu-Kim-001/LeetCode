# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        #bfs contains [node, node_num from left] of each level. 
        bfs = [[root, 0]]
        ans = 1
        while bfs:
            bfs2 = []
            for node, node_num in bfs:
                if node.left:
                    bfs2.append([node.left, node_num * 2])
                if node.right:
                    bfs2.append([node.right, node_num * 2 + 1])
            if bfs2:
                ans = max(ans, bfs2[-1][1] - bfs2[0][1] + 1)
            bfs = bfs2
        return ans