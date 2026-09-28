# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or head.next is None or k==0:
            return head
        
        curr=head
        n=1
        while curr.next:
            curr=curr.next
            n+=1

        curr.next=head
        k=k%n
        steps=n-k-1
        new_tail=head

        for _ in range(steps):
            new_tail=new_tail.next

        new_head=new_tail.next
        new_tail.next=None

        return new_head

        