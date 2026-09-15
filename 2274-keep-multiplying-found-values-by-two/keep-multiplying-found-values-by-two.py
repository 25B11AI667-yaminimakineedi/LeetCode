class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        def multiply_by_two(nums,k):
            if k not in nums:
                return k
            k=k*2
            return multiply_by_two(nums,k)
        return multiply_by_two(nums,original)
        