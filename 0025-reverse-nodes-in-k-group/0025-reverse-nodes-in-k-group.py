# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head

        grp_prev=dummy

        while True:
            kth=grp_prev

            for _ in range(k):
                if kth.next is None:
                    return dummy.next

                kth=kth.next
            grp_next=kth.next

            curr=grp_prev.next
            prev=grp_next

            while curr!=grp_next:
                next_node=curr.next
                curr.next=prev
                prev=curr
                curr=next_node

            old_start=grp_prev.next
            grp_prev.next=kth

            grp_prev=old_start