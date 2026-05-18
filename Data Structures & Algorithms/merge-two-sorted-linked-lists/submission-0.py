# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        dummy = ListNode(-1)
        tail = dummy
        
        while(head1 is not None and  head2 is not None):
            if(head1.val==head2.val):
                tail.next = head1
                head1 = head1.next
                tail = tail.next
                tail.next = head2
                head2 = head2.next
                tail = tail.next
            elif(head1.val<head2.val):
                tail.next = head1
                head1 = head1.next
                tail = tail.next
            else:
                tail.next = head2
                head2 = head2.next
                tail = tail.next
        if(head1 is not None):
            tail.next = head1
        if(head2 is not None):
            tail.next = head2
        return dummy.next
