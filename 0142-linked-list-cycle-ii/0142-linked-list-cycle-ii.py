# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=head
        seen=set()
        while fast and fast.next:
            if fast not in seen:
                seen.add(fast)
            else:
                return fast
            fast=fast.next

        return None