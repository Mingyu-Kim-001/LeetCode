# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 1
        cur = head
        while cur:
            if cur.next:
                cur = cur.next
                length += 1
            else:
                break
        small_chunk_size = length // k
        large_chunk_num = length - (small_chunk_size * k)
        
        cur = head
        ans = [None] * k
        idx = 0
        prev = None
        while cur:
            ans[idx] = cur
            cur_chunk_len = 1
            while cur_chunk_len < small_chunk_size + (1 if large_chunk_num > 0 else 0):
                cur_chunk_len += 1
                prev = cur
                cur = cur.next
            end = cur
            cur = cur.next
            end.next = None
            large_chunk_num -= 1
            idx += 1
        return ans
            