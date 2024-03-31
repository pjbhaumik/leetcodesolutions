class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        a = list(s)
        
        for i, numeral in enumerate(a):
            if numeral == 'M': a[i] = 1000
            if numeral == 'D': a[i] = 500
            if numeral == 'C': a[i] = 100
            if numeral == 'L': a[i] = 50
            if numeral == 'X': a[i] = 10
            if numeral == 'V': a[i] = 5
            if numeral == 'I': a[i] = 1
    
        i = 0
        while i < len(a)-1:
            if a[i] < a[i+1]:
                sum += a[i+1]-a[i]
                i += 2
            else:
                sum += a[i]
                i += 1
        
        if i <= len(a)-1: sum += a[i]
            
        return sum
