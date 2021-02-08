# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque,defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        bfs = deque([[root,0,0]])
        nodeOfX = defaultdict(list)
        while bfs:
            node,x,y = bfs.popleft()
            nodeOfX[x].append([node,y])
            if node.left:
                bfs.append([node.left,x-1,y-1])
            if node.right:
                bfs.append([node.right,x+1,y-1])
            
        result = []
        for x in sorted(list(nodeOfX.keys())):
            s = sorted(nodeOfX[x],key=lambda x:(-x[1],x[0].val))
            result.append([i[0].val for i in s])
        return result