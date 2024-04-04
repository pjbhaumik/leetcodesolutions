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
    
# Alternative
class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        _map = {'(':1, ')':-1}
        _str = [_map[x] for x in list(s) if x in ['(', ')']]

        _max = 0
        
        for i in range(len(_str)):
            _max = max(_max, sum(_str[:i+1]))
            
        return _max