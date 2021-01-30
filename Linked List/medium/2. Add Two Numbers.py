# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Time: O(n) Space: O(n)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        head = dummy
        rem = 0
        while l1 or l2 or rem:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + rem
            rem = val//10
            val = val%10
            head.next = ListNode(val)
            head = head.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next