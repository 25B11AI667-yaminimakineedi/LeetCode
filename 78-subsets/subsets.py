class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def subsequences(i,a,r=[]):
            if i>=len(a):
                ans.append(r.copy())
                return 
            r.append(a[i])
            subsequences(i+1,a,r)
            r.pop()
            subsequences(i+1,a,r)
        subsequences(0,nums)
        return ans