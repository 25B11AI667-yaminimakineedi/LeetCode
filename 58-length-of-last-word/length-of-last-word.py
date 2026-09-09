class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        substrings=s.split()
        n=len(substrings)
        return len(substrings[n-1])