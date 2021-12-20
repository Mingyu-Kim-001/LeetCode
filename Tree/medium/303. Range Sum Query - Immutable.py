class TreeNode:
    def __init__(self,val=0,start=None,end=None,left=None,right=None):
        self.val = val
        self.start = start
        self.end = end
        self.left = left
        self.right = right
        
    
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.segtree_root = self.build_segtree(0, len(nums)-1)
        
    def build_segtree(self, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(self.nums[start], start, end, None, None)
        mid = (start+end) // 2
        left_node = self.build_segtree(start,mid)
        right_node = self.build_segtree(mid+1, end)
        left_sum = left_node.val if left_node else 0
        right_sum = right_node.val if right_node else 0
        return TreeNode(left_sum + right_sum, start, end, left_node, right_node)
    
    def sum_helper(self, node, start, end):
        
        if start == node.start and end == node.end:
            print(start, end, node.val)
            return node.val
        
        mid = (node.start+node.end) // 2
        if end <= mid:
            return self.sum_helper(node.left, start, end)
        if mid + 1 <= start:
            return self.sum_helper(node.right, start, end)
        
        return self.sum_helper(node.left, start, mid) + self.sum_helper(node.right, mid+1, end)
        
            
    def sumRange(self, start: int, end: int) -> int:
        return self.sum_helper(self.segtree_root, start, end)