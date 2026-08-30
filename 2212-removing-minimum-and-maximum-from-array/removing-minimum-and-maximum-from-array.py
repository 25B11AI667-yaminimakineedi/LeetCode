class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return len(nums)
        min_index=0
        max_index=0
        for i in range(0,len(nums)):
            if nums[i]<nums[min_index]:
                min_index=i
            if nums[i]>nums[max_index]:
                max_index=i
        left_index=min(min_index,max_index)
        right_index=max(min_index,max_index)
        total_dels_bothends=(left_index+1)+(len(nums)-right_index)
        total_dels_front=right_index+1
        total_dels_back=len(nums)-left_index
        return min( total_dels_bothends,total_dels_front,total_dels_back)
