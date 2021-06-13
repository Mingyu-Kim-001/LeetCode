class Node:
    def __init__(self,start,end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        
class MyCalendar:
    def __init__(self):
        self.root = None
    
    def helper(self, start, end, node):
        if end <= node.start:
            if node.left:
                return self.helper(start,end,node.left)
            node.left = Node(start,end)
            return True
        
        if node.end <= start:
            if node.right:
                return self.helper(start,end,node.right)
            node.right = Node(start,end)
            return True
        
        return False
    
    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node(start,end)
            return True
        return self.helper(start,end,self.root)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)