# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        stack = [head] # first node in the linked list
        while head.next: # create a list of all nodes, so we know how many nodes there are
            head = head.next
            stack.append(head)
        
        #singly linked lists are DAGs
        #break all of the present links to prevent cycles when re-assigning nodes
        for node in stack: 
            node.next = None
        
        final = []
        midpoint = int(len(stack)/2)+(len(stack)%2)
        
        for i in range(midpoint): #calculate new assignments
            final.append(i+1)
            if (len(stack)%2 == 0) or (i != midpoint - 1):
                final.append(len(stack)-i)
                
        head = stack[0]
        
        for val in final[1:]: #implement new assignments
            head.next = stack[val-1]
            head = head.next
        return