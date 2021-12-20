# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
from collections import deque
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = deque(nestedList)
        
    def next(self) -> int:
        if self.nestedList[0].isInteger():
            return self.nestedList.popleft().getInteger()
        else:
            self.flatten()
            return self.next()
    
    def flatten(self):
        nested_nestedList = self.nestedList.popleft().getList()
        self.nestedList = deque(nested_nestedList) + self.nestedList
            
    def hasNext(self) -> bool:
        if not self.nestedList:
            return False
        if self.nestedList[0].isInteger():
            return True
        self.flatten()
        return self.hasNext()
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())