class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        score = 0
        sorted_happiness = sorted(happiness) #queue of happiness scores; O(nlogn)
        
        for i in range(k):
            happy = sorted_happiness.pop() - i #max happiness is always at the end; O(1)
            if happy <= 0:
                break
            score += happy
            
        return score