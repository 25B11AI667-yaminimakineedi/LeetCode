class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binary_search(low,high):
            if low > high:
                return low
            mid=(low+high)//2
            if target==nums[mid]:
                return mid
            elif target<nums[mid]:
                return binary_search(low,mid-1)
            else:
                return binary_search(mid+1,high)
        return binary_search(0,len(nums)-1)


        