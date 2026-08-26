class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r=[]
        for i in range(len(nums)):
            if nums[i]!=0:
                r.append(nums[i])
        no_of_zeroes=len(nums)-len(r)
        r.extend([0]*no_of_zeroes)               
        nums.clear()
        nums.extend(r)