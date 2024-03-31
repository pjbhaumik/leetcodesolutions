class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def check(x):
            if x == x[::-1]:
                return x
            
        def substring(x):
            return x[:-1]
        
        palindromes = {}
        
        if check(s):
            return s
        
        for i in range(len(s)):
            x = s[i:]
            for j in range(len(x)):
                palindrome = check(x)
                if not palindrome:
                    x = substring(x)
                elif len(palindrome) not in palindromes:
                    palindromes[len(palindrome)] = palindrome
        
        _max = max(list(palindromes.keys()))
        return palindromes[_max]