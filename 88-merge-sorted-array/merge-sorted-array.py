class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp=[]
        mid=m-1
        high=m+n-1
        left=0
        right=0
        while (left<=mid and right<n):
            if nums1[left]<=nums2[right]:
                temp.append(nums1[left])
                left+=1
            else:
                temp.append(nums2[right])
                right+=1
        while left<=mid:
            temp.append(nums1[left])
            left+=1
        while right<n:
            temp.append(nums2[right])
            right+=1
        for i in range(high+1):
            nums1[i]=temp[i]
