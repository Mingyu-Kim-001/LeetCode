# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        nodeDic = defaultdict(list)
        def DFS(node,x,y):
            if not node: return
            nodeDic[y].append([node,x])
            DFS(node.left,x+1,y-1)
            DFS(node.right,x+1,y+1)
        DFS(root,0,0)
        result = []
        for key in sorted(list(nodeDic.keys())):
            nodeDic[key].sort(key = lambda x:(x[1],x[0].val))
            result.append([i[0].val for i in nodeDic[key]])
        return result