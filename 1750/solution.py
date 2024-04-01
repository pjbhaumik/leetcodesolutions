class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        while len(s) > 1 and (s[0] == s[-1]):
            _start = s[0]
            while len(s) > 1 and (s[0] == s[-1]):
                s = s[:-1]
            while s and (s[0] == _start):
                s = s[1:]
            
        
        return len(s)