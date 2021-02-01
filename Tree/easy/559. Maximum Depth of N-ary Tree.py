#Time: O(n)
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        def DFS(node,depth):
            result = depth
            for child in node.children:
                result = max(result,DFS(child,depth+1))
            return result
        return DFS(root,1)