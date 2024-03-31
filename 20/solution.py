class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        open = ['[', '(', '{']
        close = [']', ')', '}']
        stack = []
        for i in s:
            if i in open:
                stack.append(i)
            else:
                if not stack or open[close.index(i)] != stack.pop():
                    return False
                
        return (not stack)