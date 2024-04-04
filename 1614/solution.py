class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        _str = [x for x in list(s) if x in ['(', ')']]
        counter = 0
        _max = 0
        
        while _str:
            char = _str.pop()
            if char == ')':
                counter += 1
            elif char == '(':
                counter -=1
                
            _max = max(_max, counter)
            
        return _max