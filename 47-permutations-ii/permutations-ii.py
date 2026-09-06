class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def swap_digits(i):
            if i==len(nums):
                if nums not in result:
                    result.append(nums.copy())
                    return
            for j in range(i,len(nums)):
                nums[i],nums[j]=nums[j],nums[i]
                swap_digits(i+1)
                nums[i],nums[j]=nums[j],nums[i]
        swap_digits(0)
        return result