class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        common_elements=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                common_elements.append(nums1[i])
            
        return list(set(common_elements))

