# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        headcopy = deepcopy(head)
        reverse = head
        prev = None
        curr = reverse
        next = curr
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        reverse = prev
        head = headcopy
        # print(reverse)
        while reverse != None:
            if reverse.val != head.val:
                return False
            reverse = reverse.next
            head = head.next
        return True
            
            
        