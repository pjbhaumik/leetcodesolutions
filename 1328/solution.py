class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        
        broken = ""
        
        if len(palindrome) < 2:
            return broken

        _map={}
        
        for i, char in enumerate('abcdefghijklmnopqrstuvwxyz'):
            _map[char] = i
            
        broken = palindrome[:int(len(palindrome)/2)]
        
        for i, letter in enumerate(broken):
            if _map[letter] > 0:
                return broken[:i]+'a'+broken[i+1:]+palindrome[int(len(palindrome)/2):]
        
        return broken+palindrome[int(len(palindrome)/2):-1]+'b'