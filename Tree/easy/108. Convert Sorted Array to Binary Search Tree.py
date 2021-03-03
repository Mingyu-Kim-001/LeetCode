# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        start = 0
        end = len(nums)-1
        def toBST(nums,start,end):
            if end<start: return None
            n = end-start+1
            if n==1:
                return TreeNode(nums[start])
            mid = start + (end-start)//2
            root = TreeNode(nums[mid])
            root.left = toBST(nums,start,mid-1)
            root.right = toBST(nums,mid+1,end)
            return root
        return toBST(nums,0,len(nums)-1)