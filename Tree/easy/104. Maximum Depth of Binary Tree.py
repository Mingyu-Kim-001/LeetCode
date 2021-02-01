class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def DFS(node,depth):
            if not node:
                return depth-1
            return max(DFS(node.left,depth+1),DFS(node.right,depth+1))
        return DFS(root,1)