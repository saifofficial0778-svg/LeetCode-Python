# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        prev_grp=dummy

        while True:
            kth=prev_grp

            for _ in range(k):
                kth=kth.next
                
                if kth is None:
                    return dummy.next
            next_grp=kth.next

            curr=prev_grp.next
            prev=next_grp
            while curr!=next_grp:
                next_node=curr.next
                curr.next=prev
                prev=curr
                curr=next_node
            
            old_start=prev_grp.next
            prev_grp.next=kth

            prev_grp=old_start
            
            

