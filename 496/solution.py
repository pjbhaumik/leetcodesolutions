class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hash_map = {}
        res = []
        
        for num in nums2:
            while stack and stack[-1] < num:
                hash_map[stack.pop()] = num
                
            stack.append(num)
        
        for num in nums1:
            if num in hash_map.keys():
                res.append(hash_map[num])
            else:
                res.append(-1)
        
        return res 