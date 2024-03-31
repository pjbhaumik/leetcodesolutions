# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        def big_helper(_list):
            vals = []
            def helper(_list):
                vals.append(_list.val)
                if not _list.next:
                    return
                else:
                    return helper(_list.next)
            
            helper(_list)
            
            return int(''.join([str(val) for val in vals[::-1]]))
        
        int1 = big_helper(l1)
        int2 = big_helper(l2)
        
        _answer = list(str(int1 + int2))
        
        for i, val in enumerate(_answer):
            if i == 0:
                _answer[i] = ListNode(val = val)
            else:
                _answer[i] = ListNode(val = val, next = _answer[i-1])
        
        return _answer[-1]