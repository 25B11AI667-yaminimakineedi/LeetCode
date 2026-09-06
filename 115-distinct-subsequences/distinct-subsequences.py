class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo={}
        def subsequence(i,j):
            if j==len(t):
                return 1
            if i==len(s):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if s[i]==t[j]:
                take=subsequence(i+1,j+1)
                skip=subsequence(i+1,j)
                memo[(i,j)]=take+skip
            else:
                memo[(i,j)]=subsequence(i+1,j)
            return memo[(i,j)]       
        return subsequence(0,0)
