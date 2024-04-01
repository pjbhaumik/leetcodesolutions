class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        def helper(_in):
            x = {}
            for val in list(_in):
                if val in x:
                    x[val] += 1
                else:
                    x[val] = 1
            return x
        
        xnote = helper(ransomNote)
        xbank = helper(magazine)
        
        for k, v in xnote.items():
            if k not in xbank:
                return False
            if v > xbank[k]:
                return False
            
        return True