class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        _sum = 0
        _max = sum(nums)
        
        if max(nums) < 0:
            return max(nums)
        
        
        for num in nums:
            _sum += num
            if _sum < 0:
                _sum = 0
            
            _max = max(_sum, _max)
            
            
        return _max
        