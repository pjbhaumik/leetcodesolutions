class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        shortest_word = min(strs, key = len)
        
        while len(shortest_word) > 0:
            a = 0
            for word in strs:
                if word.find(shortest_word) == 0:
                    a += 1
            if a == len(strs):
                return shortest_word
            shortest_word = shortest_word[:-1]
        return ""