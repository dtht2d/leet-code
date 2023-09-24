"""
Problem: Given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
Assume the two numbers do not contain any leading zero, except the number 0 itself.
Constraints:
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.
"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not (1 <= getLength(l1) <= 100) or not (1 <= getLength(l2) <= 100):
            raise ValueError("The number of nodes in each linked list must be in the range [1, 100].")
        dummy_head = ListNode()
        curr = dummy_head
        carry = 0
        while l1 or l2:
            #Assign value of l1 and l2
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            #Add x and y
            sum = x + y
            carry = sum // 10
            if carry > 0:
                sum = sum % 10
                curr.next = ListNode(sum)
            return dummy_head.next

s = Solution()
l1 = [2,4,3]
l2 = [5,6,4]
print(s.addTwoNumbers(l1,l2))