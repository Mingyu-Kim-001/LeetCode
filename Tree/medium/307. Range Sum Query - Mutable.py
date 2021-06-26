class Node:
    def __init__(self, start, end):
        self.right = None
        self.left = None
        self.start = start
        self.end = end
        self.total = 0

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.root = Node(0,len(nums) - 1)
        self.create_segment_tree(self.root)
        
    def create_segment_tree(self, root):
        if root.start == root.end:
            root.total = self.nums[root.start]
            return root.total
        m = (root.start + root.end) // 2
        root.left = Node(root.start, m)
        root.right = Node(m+1, root.end)
        root.total = self.create_segment_tree(root.left) + self.create_segment_tree(root.right)
        return root.total
        
    def update(self, index: int, val: int) -> None:
        def DFS(node, update_idx, update_val):
            if node.start == node.end and node.end == update_idx:
                node.total = update_val
            else:
                m = (node.start + node.end) // 2
                if update_idx <= m:
                    DFS(node.left, update_idx, update_val)
                else:
                    DFS(node.right, update_idx, update_val)
                node.total = node.left.total + node.right.total
        DFS(self.root, index, val)

    def sumRange(self, start: int, end: int) -> int:
        def sumRangeHelper(node,start,end):
            # print(start,end,node.start,node.end)
            if node.start == start and node.end == end:
                return node.total
            m = (node.start + node.end) // 2
            if end <= m:
                return sumRangeHelper(node.left, start, end)
            if m < start:
                return sumRangeHelper(node.right, start, end)
            return sumRangeHelper(node.left, start, m) + sumRangeHelper(node.right, m+1, end)
        return sumRangeHelper(self.root, start, end)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)