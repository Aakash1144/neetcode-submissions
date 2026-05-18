# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if(head == None):
            return None
        # if(head.next == None):
        #     return head
        slow = head
        fast = head
        while(fast is not None and fast.next is not None):
            fast = fast.next.next
            slow = slow.next
        print("slow",slow.val)
        #head to slow list1
        #slow.next to fast list2
        l1 = head
        l2 = slow.next
        slow.next = None
        # print("l1.val,slow.val,l2.val,fast.val",l1.val,slow.val,l2.val,fast.val)
        # now reverse the list2, we need to find
        # l2 is head and prev is tail of 2nd list
        
        temp = l2
        before = None
        # after = temp.next
        
        while(temp is not None):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        l2 = before
        # print("l2.val after reverse", l2.val)    

        dummy = ListNode(-1)
        tail = dummy
        while(l1 is not None and l2 is not None):
            tail.next = l1
            l1 = l1.next
            tail = tail.next
            print(tail.val)
            tail.next = l2
            l2 = l2.next
            tail = tail.next
            print(tail.val)
        if l1 is not None:
            tail.next = l1
        elif l2 is not None:
            tail.next = l2