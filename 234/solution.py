# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head.next:
            return True
        
        unlinked_list =[head.val]
        
        _len = 1
        while head.next:
            head = head.next
            unlinked_list.append(head.val)
            _len += 1
        
        midpoint = int(_len/2) + _len%2
        first_half = unlinked_list[:midpoint]
        second_half = unlinked_list[-midpoint:]
        
        for val in first_half:
            if val != second_half.pop():
                return False
        
        return True