'''
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        # iterate the ListNode to a list
        res = []
        while head:
            res.append(head.val)
            head = head.next
        l = len(res)
        # is it a palindrome ?
        for i in range(l // 2):
            if res[i] != res[-(i + 1)]:
                return False
        return True
