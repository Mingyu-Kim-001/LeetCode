# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        deepestCount = 0
        maxDepth= -10
        def getMaxDepth(root,depth):
            if not root.left and not root.right:
                nonlocal maxDepth
                if maxDepth<depth:
                    maxDepth = depth
                    nonlocal deepestCount
                    deepestCount = 1
                elif maxDepth==depth:
                    deepestCount+=1
            else:
                if root.left: getMaxDepth(root.left,depth+1)
                if root.right: getMaxDepth(root.right,depth+1)
        getMaxDepth(root,0)
        # print(maxDepth,deepestCount)
        
        # def numOfDeepest(root,depth):
        #     if not root:
        #         return 0
        #     if depth==maxDepth:
        #         return 1
        #     return numOfDeepest(root.left,depth+1) + numOfDeepest(root.right,depth+1)
        # deepestCount = numOfDeepest(root,0)
        
        sol = None
        def DFS(root,depth):
            nonlocal sol
            if not root:
                result=0
            elif depth==maxDepth:
                result = 1
            else:
                result = DFS(root.left,depth+1) + DFS(root.right,depth+1)
            if not sol and result==deepestCount:
                sol=root
            return result
        DFS(root,0)
        return sol