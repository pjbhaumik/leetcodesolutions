class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #filter out values larger than the target
        # xnums = [num for num in nums if num <= target]
        
        #check each element and search for target-element
        for i, num in enumerate(nums):
            partner = target-num
            if partner in nums[i+1:]:
                nums[i] = 'x'
                return [i, nums.index(partner)]
        
        return