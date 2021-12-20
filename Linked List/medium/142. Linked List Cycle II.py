# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Time: O(n), Space: O(n)
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        seen = set()
        while head:
            if head in seen:
                return head
            seen.add(head)
            head = head.next
        return None