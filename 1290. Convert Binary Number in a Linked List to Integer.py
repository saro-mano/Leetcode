# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        #reverse it
        result = 0
        prev = None
        curr = next = head
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev
        binary_multiplier = 1
        while head != None:
            result += head.val * binary_multiplier
            binary_multiplier *= 2
            head = head.next
        return result
            
        
        