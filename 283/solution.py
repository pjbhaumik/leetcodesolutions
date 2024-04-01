class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        _temp = []
        zeros = []
        while nums:
            val = nums.pop()
            if val != 0:
                _temp.append(val)
            else:
                zeros.append(0)
                
        nums += _temp[::-1] + zeros