# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Time:O(n)
class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        i = 0
        while i<len(S):
            if S[i]=="-":break
            i+=1
        root = TreeNode(val=int(S[:i]))
        stack = [[root,0]]
        while i<len(S):
            depth = 0
            while i<len(S):
                if S[i]!="-": break
                depth+=1
                i+=1
            prev = i
            while i<len(S):
                if S[i]=="-": break
                i+=1
            node = TreeNode(val=int(S[prev:i]))
            while stack and stack[-1][1]+1!=depth:
                stack.pop()
            if stack[-1][0].left: 
                stack[-1][0].right = node
            else:
                stack[-1][0].left = node
            stack.append([node,depth])
        return root