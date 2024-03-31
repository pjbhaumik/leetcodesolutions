"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head:
            _out = [[head.val, head.random]]
            i = 0
            _map = {head:i}
            while head.next:
                head = head.next
                i += 1
                _map[head] = i
                _out.append([head.val, head.random])  

            for i in range(len(_out)):
                if _out[i][1]:
                    _out[i][1] = _map[_out[i][1]]

            reverse = _out[::-1]

            for i, _set in enumerate(reverse):
                if i == 0:
                    _set.append(Node(_set[0]))
                else:
                    _set.append(Node(_set[0], next = reverse[i-1][2]))

            _final = reverse[::-1]

            for i, _set in enumerate(_final):
                if _out[i][1] is not None:
                    _final[i][2].random = _final[_out[i][1]][2]

            return _final[0][2]
        return None