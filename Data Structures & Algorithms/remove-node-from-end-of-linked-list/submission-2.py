# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if(head == None):
            return None
        if(head.next == None and n==1):
            return None
        dummy = ListNode(-1)
        dummy.next = head
        slow = dummy
        fast = dummy
        for _ in range(n):
            fast = fast.next
        # print(fast.val)

        while(fast is not None and fast.next is not None):
            fast = fast.next
            slow = slow.next
        print(slow.val)
        temp = slow.next
        slow.next = temp.next
        temp.next = None    
        return dummy.next