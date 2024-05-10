class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        medals = {0: 'Gold Medal', 1: 'Silver Medal', 2: 'Bronze Medal'}
        
        order = sorted(score, reverse = True)
        
        _map = {}

        for i, val in enumerate(order):
            if i in medals:
                _map[val] = medals[i]
            else:
                _map[val] = str(i+1)

        return [_map[val] for val in score]