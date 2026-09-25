class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if not nums:
            return 0
        current_max=nums[0]
        global_max=nums[0]
        for i in range(1,len(nums)):
            current_max=max(nums[i],nums[i]+current_max)
            if global_max<current_max:
                global_max=current_max
        return global_max