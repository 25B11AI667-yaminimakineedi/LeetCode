class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
       largest=max(nums)
       index_largest=nums.index(largest)
       for index,value in enumerate(nums):
        if index!=index_largest and largest<2*value:
            return -1
       return index_largest
        
