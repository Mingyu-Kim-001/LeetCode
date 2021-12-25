class TreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.val = 0
        self.lazy = 0
        self.left = None
        self.right = None

class MyCalendarThree:
    def __init__(self):
        self.root = TreeNode(0, 10 ** 9)
    
    def update(self, start, end, node, lazy = 0):
        
        if node.end <= start or end <= node.start:
            node.val += lazy
            node.lazy += lazy
            return node.val
        
        if start <= node.start and node.end <= end:
            node.val += 1 + lazy
            node.lazy += 1 + lazy
            return node.val
        
        m = (node.start + node.end) // 2
        if not node.left:
            node.left = TreeNode(node.start, m)
        if not node.right:
            node.right = TreeNode(m, node.end)
        node.val += lazy
        left_max = self.update(start, end, node.left, node.lazy + lazy)
        right_max = self.update(start, end, node.right, node.lazy + lazy)
        node.val = max(node.val, left_max, right_max)
        node.lazy = 0
        return node.val
    
    def book(self, start, end):
        return self.update(start, end, self.root)
        