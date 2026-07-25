# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        count=0
        while curr:
            count+=1
            curr=curr.next
        mid = count // 2
        curr=head

        for _ in range(mid):
            curr=curr.next
        return curr

       
