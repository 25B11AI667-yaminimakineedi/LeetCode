class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # A power of two must be positive and follow the bitwise rule
        return n > 0 and (n & (n - 1)) == 0
