class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        s, stack = list(s), []
        
        for i, c in enumerate(s):
            if c == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
            if c == '(':
                stack.append(i)
        
        for i in stack:
            s[i] = ''
        
        return ''.join(s)