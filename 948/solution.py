class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        score = 0
        
        while any(tokens):
            while any(token <= power for token in tokens):
                score += 1
                power -= tokens.pop(tokens.index(min(tokens))) 
            if len(tokens) > 2 and score > 0:
                score -= 1
                power += tokens.pop(tokens.index(max(tokens)))
            else:
                break

        
        return score