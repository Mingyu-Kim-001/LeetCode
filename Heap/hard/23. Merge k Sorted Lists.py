# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time: O(nlogk)
import heapq as hq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        dummy = ListNode()
        head = dummy
        remaining = sum([(1 if node else 0) for node in lists])
        while remaining:
            if not heap:
                for i,node in enumerate(lists):
                    
                    if node: hq.heappush(heap,[node.val,i,node])
            
            _,__,nextNode = hq.heappop(heap)
            head.next = nextNode
            head = head.next
            if not head.next:
                remaining-=1
            else:
                hq.heappush(heap,[head.next.val,__,head.next])
        return dummy.next