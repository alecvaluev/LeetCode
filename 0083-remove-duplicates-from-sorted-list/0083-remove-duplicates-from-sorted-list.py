# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #dummy = ListNode(None)
        #dummy.next = head
        #prev, curr = dummy, head
        
        #while curr:
        #    if curr.val == prev.val:
        #        prev.next = curr.next
        #    else:
        #        prev = curr
        #    curr = curr.next
        #
        #return dummy.next
        
        
        curr = head
        
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
            curr = curr.next
        return head