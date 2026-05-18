#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None):
            return None
        temp = head
        length = 0
        print(head.val, head.next)
        while(temp is not None):
            tail = temp
            temp = temp.next
            length = length + 1 
            print(length)
        
        print("len = ", length)

        # swap the head and tail
        temp = head
        head = tail
        tail = temp
        before = None
        after = temp.next
        for _ in range(length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return head