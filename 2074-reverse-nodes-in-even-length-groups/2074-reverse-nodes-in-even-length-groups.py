# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        group_prev = dummy
        group_len = 1

        while group_prev.next:

            group_end = group_prev
            actual_len = 0

            for _ in range(group_len):
                if group_end.next is None:
                    break

                group_end = group_end.next
                actual_len += 1

            next_group = group_end.next

            if actual_len % 2 == 0:

                curr = group_prev.next
                prev = next_group

                for _ in range(actual_len):
                    next_node = curr.next
                    curr.next = prev
                    prev = curr
                    curr = next_node

                old_start = group_prev.next
                group_prev.next = group_end

                group_prev = old_start

            else:
                group_prev = group_end

            group_len += 1

        return dummy.next



       