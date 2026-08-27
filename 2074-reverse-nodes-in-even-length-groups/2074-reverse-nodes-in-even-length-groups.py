# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head

        grp_prev=dummy
        grp_len=1

        while grp_prev.next:
            grp_end=grp_prev
            actual_len=0

            for _ in range(grp_len):
                if grp_end.next is None:
                    break
                grp_end=grp_end.next
                actual_len+=1
            grp_next=grp_end.next

            if actual_len%2==0:

                curr=grp_prev.next
                prev=grp_next

                while curr!=grp_next:
                    next_node=curr.next
                    curr.next=prev
                    prev=curr
                    curr=next_node

                old_start=grp_prev.next
                grp_prev.next=grp_end

                grp_prev=old_start
            else:
                grp_prev=grp_end
            grp_len+=1
        return dummy.next
                