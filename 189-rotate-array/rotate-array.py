class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d=k%len(nums)
        def reverse_array(arr,start,end):
            while start<=end:
                arr[start],arr[end]=arr[end],arr[start]
                start+=1
                end-=1
        reverse_array(nums,0,len(nums)-d-1)
        reverse_array(nums,len(nums)-d,len(nums)-1)
        reverse_array(nums,0,len(nums)-1)
