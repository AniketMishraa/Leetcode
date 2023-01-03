# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        a = 0
        while temp:
            a += 1
            temp = temp.next
        a = a // 2
        while a > 0:
            head = head.next
            a -= 1
        return head