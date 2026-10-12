# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:

        rev1 = self.reverse(l1)
        rev2 = self.reverse(l2)
        val1 = ""
        val2 = ""

        while rev1:
            val1 += str(rev1.val)
            rev1 = rev1.next
        
        while rev2:
            val2 += str(rev2.val)
            rev2 = rev2.next

        summ = str(int(val1) + int(val2))
        dummy = node = ListNode()
        for digit in reversed(summ):
            node.next = ListNode(int(digit))
            node = node.next
        
        return dummy.next

    

    def reverse(self, head1: ListNode | None) -> ListNode| None:
        prev = None
        curr = head1

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev