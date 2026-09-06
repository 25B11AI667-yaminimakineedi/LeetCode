class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        def subsets(i,a,r=[]):
            if i>=len(a):
                if r not in ans:
                    ans.append(r.copy())
                return
            r.append(a[i])
            subsets(i+1,a,r)
            r.pop()
            j=i+1
            while j<len(a) and a[i]==a[j]:
                j+=1
            subsets(j,a,r)
        subsets(0,nums)
        return ans