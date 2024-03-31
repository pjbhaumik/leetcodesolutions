class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0 or [int(y) for y in str(x)][::-1] != [int(y) for y in str(x)]:
            return False     
        else:
            return True